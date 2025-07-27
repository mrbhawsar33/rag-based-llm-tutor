# Python Tutor

This project is a Python programming tutor and assistant built using LlamaIndex, Mistral AI, and a Gradio interface. It can answer questions about Python, leveraging a knowledge base built from web-scraped content and PDF documents.

## Features

-   **RAG Pipeline**: Uses a Retrieval-Augmented Generation (RAG) pipeline to provide answers from a custom knowledge base.
-   **Multi-Source Knowledge**: Ingests data from both web pages and PDF files.
-   **Context-Aware**: Remembers conversation history to answer follow-up questions.
-   **Interactive UI**: A user-friendly web interface built with Gradio.
-   **Persistent Storage**: Uses ChromaDB to store vector embeddings, avoiding re-processing on each run.

---

## Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

-   Python 3.10 or higher.

### 2. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/mrbhawsar33/rag-based-llm-tutor.git
cd rag-based-llm-tutor
```

### 3. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

**On macOS / Linux:**

```bash
python3 -m venv my_venv
source my_venv/bin/activate
```

**On Windows:**

```bash
python -m venv my_venv
.\my_venv\Scripts\activate
```

### 4. Set Up API Keys

This project requires an API key from Mistral AI.

1.  Create a file named `.env` in the root of the project directory.
2.  Add your API key to the `.env` file as follows:

    ```
    MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY_HERE"
    ```

**Important**: Add the `.env` file to your `.gitignore` to ensure your keys are not committed to version control.

### 5. Install Dependencies

Install all the required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 6. Project structure

├── /data/
│   ├── /pdfs/             # Place your PDF files here
│   └── /chroma_db/        # The vector database will be stored here
├── /app/
│   ├── agent.py             # Place your PDF files here
│   └── config.py
│   └── main.py
│   └── tutor.py
│   └── ui.py
│   └── utils.py
├── /notebooks/            # Jupyter notebooks with initial exploratory modular experiments
├── .env
├── requirements.txt
├── README.md

### 7. Run the application

```bash
uvicorn app.main:app --reload --root-path / 
```