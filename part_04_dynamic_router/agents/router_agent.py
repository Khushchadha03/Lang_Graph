from shared.utils.azure_openai import run_llm_with_system
from part_04_dynamic_router.routers.dynamic_router import DynamicRouter

class RouterAgent:
    """Agent that uses dynamic routing to handle different types of requests."""

    def __init__(self, name: str):
        self.name = name
        self.router = DynamicRouter()

    def run_with_routing(self, prompt: str) -> str:
        """Route and process the request."""
        route = self.router.route_request(prompt)
        
        specialist_prompts = {
            "math": "You are a mathematics expert. Solve problems step by step with clear explanations.",
            "text": "You are a text analysis expert. Provide detailed text insights and linguistic analysis.",
            "research": "You are a research assistant. Provide accurate, well-sourced information.",
            "creative": "You are a creative writing assistant. Be imaginative and engaging.",
            "tools": "You are a tools specialist. Help with data processing and tool recommendations."
        }
        
        system_prompt = specialist_prompts.get(route, specialist_prompts["research"])
        response = run_llm_with_system(system_prompt, prompt)
        
        return f"[{route.upper()} SPECIALIST]: {response}"