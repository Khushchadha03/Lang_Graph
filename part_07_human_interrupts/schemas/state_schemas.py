from typing import List, Optional
from pydantic import BaseModel, Field

class InterruptState(BaseModel):
    """State that can be paused for human feedback."""
    input: str = Field(..., description="User input prompt")
    output: Optional[str] = Field(None, description="Agent response")
    history: List[str] = Field(default_factory=list, description="Conversation history")
    topic: Optional[str] = Field(None, description="Current conversation topic")
    awaiting_human: bool = Field(default=False, description="Whether the agent is waiting for human input")
    human_feedback: Optional[str] = Field(None, description="Feedback provided by a human operator")
