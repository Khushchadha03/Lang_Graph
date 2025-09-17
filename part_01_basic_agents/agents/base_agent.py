from shared.utils.azure_openai import run_llm

class BaseAgent:
    """A simple LangGraph-style agent wrapper around Azure OpenAI."""

    def __init__(self, name: str) -> None:
        self.name: str = name

    def run(self, prompt: str) -> str:
        """Execute the agent with a given prompt."""
        return run_llm(prompt)