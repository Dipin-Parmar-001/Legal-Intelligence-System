from dotenv import load_dotenv
load_dotenv()

import os
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from langchain_community.tools import tool
from rich import print

@tool
def search_tool(query : str) -> str:
    """Search the web and return summarized real time data, used for getting real time data by web searching"""
    
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    response = tavily_client.search(
        search_depth="advanced",
        max_results=6,
        query=query
    )

    result = response.get("results", [])

    final_output = []

    for res in result:
        title = res.get("title", "")
        url = res.get("url", "")
        content = res.get("content", "")

        final_output.append(f"""
Title: {title}
URL: {url}
Snippet: {content}
""")
    return "\n\n".join(final_output)

@tool
def scrape_info(url : str) -> str:
    """Scrape web page and return cleaned text output"""
    try:
        headers = {"User-Agent": "Mozila/5.0"}

        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            return "Failed to fetch the page"
        
        soup = BeautifulSoup(response.text, "lxml")

        for tag in soup(["script", "style", "noscript", "header", "footer"]):
            tag.decompose()
        
        text = soup.get_text(separator=" ", strip=True)

        return text[:1000]
    
    except Exception as e:
        return f"Scraping Error: {str(e)}"
    