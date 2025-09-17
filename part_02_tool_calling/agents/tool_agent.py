from typing import Callable, Dict
from shared.utils.azure_openai import run_llm
from part_02_tool_calling.utils.tools import calculator, text_analyzer, string_transformer

class ToolAgent:
    """Agent that can call external tools based on instructions."""

    def __init__(self, name: str):
        self.name = name
        self.tools: Dict[str, Callable[[str], str]] = {
            "calculator": calculator,
            "text_analyzer": text_analyzer,
            "string_transformer": string_transformer
        }

    def run_with_tools(self, prompt: str, tool_name: str = None) -> str:
        """Execute with optional tool calling."""
        if tool_name and tool_name in self.tools:
            return self.tools[tool_name](prompt)
        else:
            return run_llm(prompt)