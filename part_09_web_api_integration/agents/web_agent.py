from shared.utils.azure_openai import run_llm
from part_09_web_api_integration.services.wikipedia_service import fetch_wikipedia_summary
from part_09_web_api_integration.services.duckduckgo_service import fetch_duckduckgo_summary

class WebIntegrationAgent:
    """Agent that fetches context from Wikipedia & DuckDuckGo, then queries GPT."""

    def __init__(self, name: str = "WebAgent"):
        self.name = name

    def run_with_web_context(self, query: str) -> dict:
        wiki_summary = fetch_wikipedia_summary(query)
        ddg_summary = fetch_duckduckgo_summary(query)

        combined_context = f"Wikipedia: {wiki_summary}\nDuckDuckGo: {ddg_summary}"

        # Send to GPT-4o (Azure OpenAI)
        llm_response = run_llm(
            f"Here is combined context:\n{combined_context}\n\n"
            f"Now answer the user query: {query}"
        )

        return {
            "wikipedia": wiki_summary,
            "duckduckgo": ddg_summary,
            "final_answer": llm_response
        }
