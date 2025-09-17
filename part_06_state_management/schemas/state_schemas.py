from typing import List, Optional
from pydantic import BaseModel, Field

class ConversationState(BaseModel):
    """Defines a structured state for agents with memory and context."""
    input: str = Field(..., description="User input prompt")
    output: Optional[str] = Field(None, description="Agent response")
    history: List[str] = Field(default_factory=list, description="Conversation history")
    topic: Optional[str] = Field(None, description="Current conversation topic")
