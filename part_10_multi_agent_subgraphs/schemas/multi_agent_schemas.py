from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum

class TaskType(str, Enum):
    RESEARCH = "research"
    ANALYSIS = "analysis" 
    SYNTHESIS = "synthesis"

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class AgentTask(BaseModel):
    """Individual task for an agent."""
    id: str
    task_type: TaskType
    content: str
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class MultiAgentState(BaseModel):
    """State shared across all agents in the multi-agent system."""
    original_query: str
    current_phase: TaskType = TaskType.RESEARCH
    tasks: List[AgentTask] = Field(default_factory=list)
    research_results: List[str] = Field(default_factory=list)
    analysis_results: List[str] = Field(default_factory=list)
    synthesis_result: Optional[str] = None
    final_output: Optional[str] = None
    completed_phases: List[TaskType] = Field(default_factory=list)
    error_messages: List[str] = Field(default_factory=list)