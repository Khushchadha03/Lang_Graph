import requests
import urllib.parse

def fetch_wikipedia_summary(query: str) -> str:
    """Fetch a short summary from Wikipedia API."""
    formatted_query = urllib.parse.quote(query.replace(" ", "_"))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_query}"
    response = requests.get(url, headers={"User-Agent": "LangGraphBot/1.0"})
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No summary found.")
    return f"Wikipedia fetch failed ({response.status_code})."
