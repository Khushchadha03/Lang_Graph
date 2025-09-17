from typing import Callable, Dict
from shared.utils.azure_openai import run_llm, run_llm_with_system
from part_02_tool_calling.utils.tools import calculator, text_analyzer, string_transformer, random_number_generator, word_counter

class DecisionAgent:
    """Agent that decides when to call a tool or use the LLM."""

    def __init__(self, name: str):
        self.name = name
        self.tools: Dict[str, Callable[[str], str]] = {
            "calculator": calculator,
            "text_analyzer": text_analyzer,
            "string_transformer": string_transformer,
            "random_number_generator": random_number_generator,
            "word_counter": word_counter
        }

    def decide_action(self, prompt: str) -> str:
        """Use LLM to decide which action to take."""
        system_prompt = """You are a routing assistant. Given a user input, decide which tool to use:
        - calculator: for mathematical calculations
        - text_analyzer: for analyzing text properties 
        - string_transformer: for transforming text
        - random_number_generator: for generating random numbers
        - word_counter: for counting words and text statistics
        - llm: for general conversation
        
        Respond with only the tool name."""
        
        decision = run_llm_with_system(system_prompt, prompt)
        return decision.strip().lower()

    def run_with_decision(self, prompt: str) -> str:
        """Choose a tool or fallback to LLM."""
        action = self.decide_action(prompt)

        if action in self.tools:
            return self.tools[action](prompt)
        else:
            return run_llm(prompt)