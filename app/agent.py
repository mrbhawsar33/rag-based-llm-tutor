import os
import re
import requests
from bs4 import BeautifulSoup
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.mistralai import MistralAI
from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from app.config import MISTRAL_API_KEY, LLM_MODEL

def get_latest_python_releases() -> str:
    """
    Scrapes the official Python downloads page to find the latest Python releases.
    """
    url = "https://www.python.org/downloads/"
    print(f"Scraping {url} to find latest Python releases...")
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        releases = []
        
        # Find the main download button (latest release)
        main_button = soup.find('a', class_='button', string=re.compile(r'Download Python'))
        if main_button and main_button.string:
            version_match = re.search(r'(\d+\.\d+\.\d+)', main_button.string)
            if version_match:
                releases.append(version_match.group(1))

        # Find other recent release versions from the releases list
        release_links = soup.find_all('a', href=re.compile(r'/downloads/release/python-\d+'))
        
        for link in release_links[:10]:  # Check first 10 links
            version_match = re.search(r'python-(\d+\.\d+\.\d+(?:[ab]\d+|rc\d+)?)', link.get('href', ''))
            if version_match:
                version = version_match.group(1)
                if version not in releases:  # Avoid duplicates
                    releases.append(version)

        # Get the latest releases (limit to reasonable number)
        latest_releases = releases[:5]  # Top 5 latest releases
        
        if latest_releases:
            result = f"Latest Python releases found: {', '.join(latest_releases)}"
            print(f"Found {len(latest_releases)} latest releases")
        else:
            result = "No releases found on the downloads page."
            print("No releases found")
            
        return result

    except requests.exceptions.RequestException as e:
        print(f"Error scraping Python downloads page: {e}")
        return f"An error occurred while trying to fetch Python releases: {e}"

# Create tools for the agent
releases_tool = FunctionTool.from_defaults(fn=get_latest_python_releases, name="python_releases_scraper")

# Tool to perform web search using DuckDuckGo
duckduckgo_search = DuckDuckGoSearchToolSpec()
search_tools = duckduckgo_search.to_tool_list()

def get_python_version_info(prompt: str = None) -> str:
    """
    An AI agent that retrieves the latest Python releases.
    """
    if not MISTRAL_API_KEY:
        return "MISTRAL_API_KEY not configured. Cannot create agent."

    # Use a default structured prompt if none provided
    if not prompt or not prompt.strip():
        prompt = """
        Your task is to find the latest Python releases. Follow these steps:
        1. Use the python_releases_scraper tool to get releases from the official downloads page
        2. If needed, search for "Python latest releases" or "Python downloads" for additional information
        3. Provide a clean list of the latest Python release versions found
        
        Focus only on version numbers - present them in a clear, organized format.
        """

    try:
        agent_llm = MistralAI(model=LLM_MODEL, api_key=MISTRAL_API_KEY)

        # Combine all tools
        all_tools = [releases_tool] + search_tools
        
        agent = ReActAgent.from_tools(
            tools=all_tools,
            llm=agent_llm,
            verbose=True,
            max_iterations=10,  # Simplified task needs fewer iterations
            max_function_calls=5   # Fewer function calls needed
        )
        
        print("Agent starting latest releases retrieval...")
        response = agent.chat(prompt)
        print("Agent task completed.")
        return str(response)

    except Exception as e:
        print(f"An error occurred while running the agent: {e}")
        return f"An error occurred while running the agent: {e}"