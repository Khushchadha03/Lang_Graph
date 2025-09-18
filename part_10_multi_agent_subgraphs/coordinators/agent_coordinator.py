from typing import Dict, Any
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, TaskType

class AgentCoordinator:
    """Coordinates the execution of multiple agent subgraphs."""
    
    def __init__(self):
        self.execution_order = [TaskType.RESEARCH, TaskType.ANALYSIS, TaskType.SYNTHESIS]
    
    def should_proceed_to_next_phase(self, state: MultiAgentState, current_phase: TaskType) -> bool:
        """Determine if the system should proceed to the next phase."""
        if current_phase == TaskType.RESEARCH:
            return len(state.research_results) > 0 and TaskType.RESEARCH in state.completed_phases
        elif current_phase == TaskType.ANALYSIS:
            return len(state.analysis_results) > 0 and TaskType.ANALYSIS in state.completed_phases
        elif current_phase == TaskType.SYNTHESIS:
            return state.synthesis_result is not None
        return False
    
    def get_execution_summary(self, state: MultiAgentState) -> Dict[str, Any]:
        """Get a summary of the multi-agent execution."""
        return {
            "query": state.original_query,
            "phases_completed": [phase.value for phase in state.completed_phases],
            "total_tasks": len(state.tasks),
            "successful_tasks": len([task for task in state.tasks if task.status.value == "completed"]),
            "errors": state.error_messages,
            "has_final_output": state.final_output is not None
        }