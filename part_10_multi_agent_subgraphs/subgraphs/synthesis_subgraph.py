from langgraph.graph import StateGraph, START, END
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, AgentTask, TaskType, TaskStatus
from part_10_multi_agent_subgraphs.agents.synthesis_agent import SynthesisAgent

def build_synthesis_subgraph():
    """Build the synthesis subgraph."""
    synthesis_agent = SynthesisAgent()
    
    def synthesis_node(state: MultiAgentState) -> MultiAgentState:
        """Execute synthesis phase."""
        if not state.research_results or not state.analysis_results:
            state.error_messages.append("Missing research or analysis results for synthesis")
            return state
        
        # Create synthesis task
        synthesis_task = AgentTask(
            id="synthesis_1",
            task_type=TaskType.SYNTHESIS,
            content=state.original_query,
            status=TaskStatus.IN_PROGRESS
        )
        
        # Process the task with all previous results
        completed_task = synthesis_agent.process_task(
            synthesis_task, 
            state.research_results, 
            state.analysis_results
        )
        
        # Update state
        state.tasks.append(completed_task)
        if completed_task.status == TaskStatus.COMPLETED:
            state.synthesis_result = completed_task.result
            state.final_output = completed_task.result
            state.completed_phases.append(TaskType.SYNTHESIS)
        else:
            state.error_messages.append(f"Synthesis failed: {completed_task.result}")
        
        return state
    
    workflow = StateGraph(MultiAgentState)
    workflow.add_node("synthesis", synthesis_node)
    workflow.add_edge(START, "synthesis")
    workflow.add_edge("synthesis", END)
    
    return workflow.compile()