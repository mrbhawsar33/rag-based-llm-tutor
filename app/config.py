import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- API Keys ---
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# --- Model Names ---
LLM_MODEL = "codestral-latest"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# --- File Paths ---
PDF_DIR = "data/pdfs"
DB_DIR = "data/chroma_db"

# --- ChromaDB Settings ---
COLLECTION_NAME = "python_docs"

# --- Tutor Settings ---
SIMILARITY_TOP_K = 3
MAX_HISTORY = 5