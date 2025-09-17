from typing import List, Dict, Any
from datetime import datetime

class ConversationMemory:
    """Manages conversation history and context."""

    def __init__(self, max_messages: int = 50):
        self.max_messages = max_messages
        self.messages: List[Dict[str, Any]] = []
        self.session_start = datetime.now()

    def add_message(self, role: str, content: str, metadata: Dict[str, Any] = None) -> None:
        """Add a message to memory."""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        
        self.messages.append(message)
        
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get_context(self, last_n: int = 10) -> str:
        """Get conversation context as a formatted string."""
        recent_messages = self.messages[-last_n:] if self.messages else []
        
        context_parts = []
        for msg in recent_messages:
            context_parts.append(f"{msg['role']}: {msg['content']}")
        
        return "\n".join(context_parts)

    def get_summary(self) -> str:
        """Get a summary of the conversation."""
        if not self.messages:
            return "No conversation history."
        
        total_messages = len(self.messages)
        session_duration = datetime.now() - self.session_start
        
        return f"Conversation started {session_duration.seconds//60}m ago. {total_messages} messages exchanged."

    def clear_memory(self) -> None:
        """Clear all conversation memory."""
        self.messages = []

    def get_topics_discussed(self) -> List[str]:
        """Extract main topics from conversation history."""
        if not self.messages:
            return []
        
        topics = []
        for msg in self.messages[-10:]:  # Look at recent messages
            if msg['role'] == 'user' and len(msg['content']) > 10:
                # Simple topic extraction - first few words
                words = msg['content'].split()[:3]
                topic = ' '.join(words)
                if topic not in topics:
                    topics.append(topic)
        
        return topics[-5:]  # Return last 5 unique topics