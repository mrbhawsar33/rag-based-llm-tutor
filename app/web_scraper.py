"""
A simple web scraper to fetch and preprocess content from a list of URLs.
"""
import re
import requests
from bs4 import BeautifulSoup
from typing import List
from llama_index.core import Document
from app.utils import preprocess_text

def scrape_and_process_urls(urls: List[str]) -> List[Document]:
    """
    Scrapes a list of websites, preprocesses their content, and returns a list
    of LlamaIndex Document objects.

    Args:
        urls: A list of URLs to scrape.

    Returns:
        A list of Document objects containing the scraped and cleaned content.
    """
    web_documents = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    for url in urls:
        print(f"Scraping content from: {url}")
        try:
            response = requests.get(url, headers=headers, timeout=20)
            response.raise_for_status()  # Raise an exception for bad status codes

            soup = BeautifulSoup(response.content, 'html.parser')

            # Remove script and style elements to clean up the content
            for script_or_style in soup(["script", "style"]):
                script_or_style.decompose()

            # Get the raw text from the page
            raw_text = soup.get_text()

            # Preprocess the text to make it cleaner for the LLM
            cleaned_text = preprocess_text(raw_text)

            if cleaned_text:
                # Create a LlamaIndex Document object
                doc = Document(
                    text=cleaned_text,
                    metadata={"source": "web", "url": url}
                )
                web_documents.append(doc)
                print(f"Successfully scraped and processed {url}")
            else:
                print(f"Warning: No content extracted from {url} after cleaning.")

        except requests.exceptions.RequestException as e:
            print(f"Error scraping {url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while processing {url}: {e}")

    return web_documents
