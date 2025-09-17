from shared.utils.azure_openai import run_llm_with_system
from part_05_memory.memory.conversation_memory import ConversationMemory

class MemoryAgent:
    """Agent with conversation memory capabilities."""

    def __init__(self, name: str):
        self.name = name
        self.memory = ConversationMemory()

    def run_with_memory(self, prompt: str) -> str:
        """Process with conversation context."""
        self.memory.add_message("user", prompt)
        
        context = self.memory.get_context()
        topics = self.memory.get_topics_discussed()
        
        system_prompt = f"""You are a helpful assistant with access to conversation history.
                        Recent conversation:
                        {context}

                        Recent topics discussed: {', '.join(topics) if topics else 'None'}

                        Respond naturally, referencing previous context when relevant. Build upon earlier parts of our conversation."""

        response = run_llm_with_system(system_prompt, prompt)
        
        self.memory.add_message("assistant", response)
        
        return response

    def get_memory_summary(self) -> str:
        """Get a summary of conversation memory."""
        return self.memory.get_summary()

    def clear_memory(self) -> None:
        """Clear conversation memory."""
        self.memory.clear_memory()