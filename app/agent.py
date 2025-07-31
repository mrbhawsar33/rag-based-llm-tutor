"""Defines the AI agent for fetching Python release information."""

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.mistralai import MistralAI
from app.config import MISTRAL_API_KEY, LLM_MODEL
# from mistralai.error import MistralAPIException, MistralConnectionException

def get_latest_python_version_and_features() -> str:
    """
    Scrapes the official Python website to find the latest stable release,
    then navigates to that version's release page and extracts the content
    between the 'Release Date' and 'Full Changelog' sections.
    """
    try:
        # --- Step 1: Find the latest version and construct the release page URL ---
        downloads_url = "https://www.python.org/downloads/"
        print(f"Scraping {downloads_url} to find the latest version...")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(downloads_url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        latest_version_tag = soup.find('a', class_='button', string=re.compile(r'Download Python'))
        if not latest_version_tag:
            return "Could not find the download button for the latest Python version."

        version_match = re.search(r'(\d+\.\d+\.\d+)', latest_version_tag.string)
        if not version_match:
            return "Could not extract the version number from the download button."
        
        latest_version = version_match.group(1)
        version_for_url = latest_version.replace('.', '')
        release_page_url = f"https://www.python.org/downloads/release/python-{version_for_url}/"
        print(f"Found latest version: {latest_version}. Navigating to release page: {release_page_url}")

        # --- Step 2: Scrape the release page for content between two points ---
        response = requests.get(release_page_url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the starting point: the <strong> tag with "Release Date:"
        start_node = soup.find('strong', string=re.compile(r'Release Date:'))
        if not start_node:
            return f"Could not find the 'Release Date' section on page: {release_page_url}"

        # Find the ending point: the <a> tag with "Full Changelog"
        end_node_link = soup.find('a', string='Full Changelog')
        if not end_node_link:
            return f"Could not find the 'Full Changelog' link on page: {release_page_url}"
        # The actual end node is likely the parent paragraph or div of the link
        end_node = end_node_link.find_parent('p') or end_node_link

        # Collect all content between the start and end nodes
        content_parts = []
        for sibling in start_node.find_all_next():
            if sibling == end_node:
                break
            # We only want to capture text from specific, meaningful tags
            if sibling.name in ['p', 'h2', 'h3', 'ul', 'ol', 'li']:
                content_parts.append(sibling.get_text(separator=' ', strip=True))

        if not content_parts:
            return f"Successfully found version {latest_version}, but could not parse content between 'Release Date' and 'Full Changelog'."

        # --- Step 3: Format and return the final result ---
        release_content = "\n\n".join(content_parts)
        return (
            f"The latest stable Python version is **{latest_version}**.\n\n"
            f"Here is the content from the release page:\n\n{release_content}"
        )

    except requests.exceptions.RequestException as e:
        return f"A network error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred during scraping: {e}"

# Create a single, powerful tool for the agent
python_info_tool = FunctionTool.from_defaults(fn=get_latest_python_version_and_features,
                                              name="get_python_release_info")

def get_python_version_info(prompt: str = None) -> str:
    """
    An AI agent that retrieves the latest Python release and its major features.
    """
    if not MISTRAL_API_KEY:
        return "MISTRAL_API_KEY not configured. Cannot create agent."

    # The prompt is now simpler as the tool handles the entire workflow
    if not prompt or not prompt.strip():
        prompt = "Get the latest stable Python release and its three major new features."

    try:
        agent_llm = MistralAI(model=LLM_MODEL, api_key=MISTRAL_API_KEY)

        # The agent now only needs one tool
        agent = ReActAgent.from_tools(
            tools=[python_info_tool],
            llm=agent_llm,
            verbose=True
        )

        print("Agent starting task...")
        response = agent.chat(prompt)
        print("Agent task completed.")
        return str(response)

    # except MistralAPIException as e:
    #     print(f"Error communicating with Mistral AI API: {e}")
    #     return "An error occurred with the Mistral AI service. Please check your API key or try again later."
    # except MistralConnectionException as e:
    #     print(f"Network connection error to Mistral AI: {e}")
    #     return "Could not connect to the Mistral AI service. Please check your internet connection."
    except Exception as e:
        print(f"An error occurred while running the agent: {e}")
        return f"An error occurred while running the agent: {e}"
