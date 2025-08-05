"""Contains the logic for the RAG-based AI tutor."""

import os
from typing import List
import chromadb

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    Settings,
    Document,
    StorageContext
)
from llama_index.llms.mistralai import MistralAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from app.config import (
    MISTRAL_API_KEY,
    LLM_MODEL,
    EMBED_MODEL,
    PDF_DIR,
    URL_DIR,
    DB_DIR,
    COLLECTION_NAME,
    SIMILARITY_TOP_K,
    MAX_HISTORY
)
from app.utils import preprocess_text
from app.web_scraper import scrape_and_process_urls

class Tutor:
    """
    A RAG-based AI Tutor for Python programming.
    """
    def __init__(self):
        self._setup_models()
        self.query_engine = self._load_query_engine()
        self.conversation_history = []
        self.max_history = MAX_HISTORY

    def _setup_models(self):
        """Initializes and configures the LLM and embedding models."""
        system_prompt = (
            "You are an expert Python programming tutor. Your primary function is to answer "
            "questions strictly based on the provided context documents. You must not use any "
            "external knowledge. "
            "If the answer to a question cannot be found in the provided context, you must state "
            "clearly: 'I cannot answer this question based on the provided documents.' "
            "Do not attempt to guess, infer, or use any information outside of the given text. "
            "Do not hallucinate or create information. "
            "When the answer is in the context, provide clear, step-by-step explanations and "
            "practical examples."
        )

        if not MISTRAL_API_KEY:
            raise ValueError("MISTRAL_API_KEY not found in environment variables.")

        Settings.llm = MistralAI(
            model=LLM_MODEL,
            api_key=MISTRAL_API_KEY,
            system_prompt=system_prompt
        )
        Settings.embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL)
        print("LLM and embedding models initialized.")

    def _load_documents(self) -> List[Document]:
        """Loads and preprocesses documents from PDF directory and web sources."""
        documents = []

        # 1. Load and process local PDF documents
        if os.path.exists(PDF_DIR):
            pdf_docs = SimpleDirectoryReader(PDF_DIR).load_data()
            preprocessed_pdf_docs = [
                Document(text=preprocess_text(doc.text), metadata=doc.metadata)
                for doc in pdf_docs
            ]
            documents.extend(preprocessed_pdf_docs)
            print(f"Loaded and preprocessed {len(preprocessed_pdf_docs)} PDF documents.")
        else:
            print(f"PDF directory not found at {PDF_DIR}. No local PDF docs will be loaded.")

        # 2. Load URLs from file and scrape web content
        urls_to_scrape = []
        urls_file_path = os.path.join(URL_DIR, "urls.txt")

        if os.path.exists(urls_file_path):
            print(f"Loading URLs from {urls_file_path}...")
            with open(urls_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        urls_to_scrape.append(line)
            print(f"Found {len(urls_to_scrape)} URLs to scrape.")
        else:
            print(f"URLs file not found at {urls_file_path}. No web content will be scraped.")

        if urls_to_scrape:
            web_docs = scrape_and_process_urls(urls_to_scrape)
            if web_docs:
                documents.extend(web_docs)
                print(f"Added {len(web_docs)} web document(s) to the knowledge base.")

        print(f"Total documents loaded for knowledge base: {len(documents)}")
        return documents

    def _load_query_engine(self):
        """Creates or loads a vector index and returns a query engine."""
        chroma_client = chromadb.PersistentClient(path=DB_DIR)

        # For simplicity, we will always rebuild the index if web content is included.
        # This ensures the latest web content is always used.
        print("Rebuilding vector index to ensure fresh content...")
        try:
            chroma_client.delete_collection(name=COLLECTION_NAME)
            print(f"Cleared existing collection: '{COLLECTION_NAME}'")
        except Exception:
            print(f"No existing collection named '{COLLECTION_NAME}' to clear.")

        chroma_collection = chroma_client.get_or_create_collection(COLLECTION_NAME)
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        documents = self._load_documents()
        if not documents:
            print("No documents found to build the index. The tutor will have no knowledge.")
            return None

        vector_index = VectorStoreIndex.from_documents(
            documents,
            storage_context=storage_context,
            show_progress=True
        )
        print("New vector index created and persisted.")

        return vector_index.as_query_engine(
            similarity_top_k=SIMILARITY_TOP_K,
            response_mode="compact"
        )

    def add_to_history(self, question: str, answer: str):
        """Adds a question-answer pair to the conversation history."""
        self.conversation_history.append({'question': question, 'answer': answer})
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]

    def get_context_string(self) -> str:
        """Formats the conversation history into a string for the LLM."""
        if not self.conversation_history:
            return ""

        context = "\nPrevious conversation context:\n"
        for i, entry in enumerate(self.conversation_history, 1):
            context += f"Q{i}: {entry['question']}\n"
            context += f"A{i}: {entry['answer'][:200]}...\n\n"
        return context

    def clear_history(self):
        """Clears the conversation history."""
        self.conversation_history = []

    def ask_question(self, question: str, use_context: bool = True) -> str:
        """Queries the RAG pipeline with a user's question."""
        if not self.query_engine:
            return "Query engine is not available. Please check document sources."

        if not question or not question.strip():
            return "Please enter a question."

        question_lower = question.lower()
        if not use_context and ("previous question" in question_lower or "last question" in
                                question_lower or "what did i ask" in question_lower):
            return "I cannot answer that because conversation history is currently turned off. "\
                "Please check the 'Remember Conversation History' box if you'd like me to "\
                "remember past questions."

        enhanced_question = question
        if use_context:
            context_string = self.get_context_string()
            if context_string:
                enhanced_question = f"{context_string}\nCurrent question: {question}"

        response = self.query_engine.query(enhanced_question)
        answer = str(response)

        if use_context:
            self.add_to_history(question, answer)

        return answer
