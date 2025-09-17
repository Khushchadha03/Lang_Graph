from shared.utils.azure_openai import run_llm_with_system
from part_06_state_management.schemas.state_schemas import ConversationState

class StatefulAgent:
    """Agent that operates with structured state management."""

    def __init__(self, name: str):
        self.name = name

    def run_with_state(self, state: ConversationState) -> ConversationState:
        """Process user input and update structured state."""
        system_prompt = f"""You are a helpful assistant with access to conversation state.
                        Conversation history:
                        {chr(10).join(state.history)}
                        Current topic: {state.topic or 'Not set'}
                        Respond naturally and keep the context consistent."""
        response = run_llm_with_system(system_prompt, state.input)

        # Update the state
        state.history.append(f"User: {state.input}")
        state.history.append(f"Assistant: {response}")

        # Simple topic inference: first 3 words of the latest user input
        if not state.topic and len(state.input.split()) >= 3:
            state.topic = " ".join(state.input.split()[:3])

        state.output = response
        return state
