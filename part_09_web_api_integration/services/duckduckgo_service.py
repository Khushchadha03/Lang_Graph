import requests
import time

def fetch_duckduckgo_summary(query: str, retries: int = 3, backoff: float = 1.5) -> str:
    """Fetch abstract from DuckDuckGo Instant Answer API with retry + fallback."""
    url = "https://api.duckduckgo.com/"
    params = {"q": query, "format": "json"}

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, params=params, headers={"User-Agent": "LangGraphBot/1.0"})
            if response.status_code == 200:
                data = response.json()
                if data.get("AbstractText"):
                    return data["AbstractText"]
                elif data.get("RelatedTopics"):
                    return data["RelatedTopics"][0].get("Text", "No DuckDuckGo summary found.")
                else:
                    return "No DuckDuckGo summary found."
            else:
                print(f"⚠️ DuckDuckGo attempt {attempt} failed with status {response.status_code}")
        except Exception as e:
            print(f"⚠️ DuckDuckGo attempt {attempt} failed: {e}")

        # Exponential backoff before retry
        time.sleep(backoff * attempt)

    return "(DuckDuckGo unavailable, using only Wikipedia)"
