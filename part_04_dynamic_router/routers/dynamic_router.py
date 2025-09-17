from typing import Dict
from shared.utils.azure_openai import run_llm_with_system

class DynamicRouter:
    """Routes requests to different agents based on content analysis."""

    def __init__(self):
        self.route_descriptions = {
            "math": "Mathematical calculations, equations, number problems",
            "text": "Text analysis, writing, language tasks",
            "research": "Information gathering, fact-checking, general knowledge",
            "creative": "Creative writing, stories, poems, brainstorming",
            "tools": "Tool usage, data processing, transformations"
        }

    def route_request(self, user_input: str) -> str:
        """Determine the best route for the user input."""
        system_prompt = f"""You are a smart router. Given a user input, determine which specialist to route to:

Available specialists:
{chr(10).join([f"- {k}: {v}" for k, v in self.route_descriptions.items()])}

Respond with only the specialist name (math/text/research/creative/tools)."""

        route = run_llm_with_system(system_prompt, user_input)
        selected_route = route.strip().lower()
        
        if selected_route not in self.route_descriptions:
            selected_route = "research"  # default fallback
            
        return selected_route