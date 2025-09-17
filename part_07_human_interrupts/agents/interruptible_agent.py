from shared.utils.azure_openai import run_llm_with_system
from part_07_human_interrupts.schemas.state_schemas import InterruptState

class InterruptibleAgent:
    """Agent that can pause for human approval or correction."""

    def __init__(self, name: str):
        self.name = name

    def run_with_interrupts(self, state: InterruptState) -> InterruptState:
        system_prompt = f"""You are an assistant with the ability to pause for human oversight.
        
Conversation history:
{chr(10).join(state.history)}

Topic: {state.topic or 'Not set'}"""

        response = run_llm_with_system(system_prompt, state.input)

        # Simple trigger rule: if response contains sensitive action words, request human check
        if any(keyword in response.lower() for keyword in ["delete", "approve payment", "shutdown"]):
            state.awaiting_human = True
            state.output = f"[HUMAN APPROVAL REQUIRED] Suggested response: {response}"
        else:
            state.history.append(f"User: {state.input}")
            state.history.append(f"Assistant: {response}")
            state.output = response
            if not state.topic and len(state.input.split()) >= 3:
                state.topic = " ".join(state.input.split()[:3])
        
        return state
