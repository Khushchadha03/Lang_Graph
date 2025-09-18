from langgraph.graph import StateGraph, START, END
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, AgentTask, TaskType, TaskStatus
from part_10_multi_agent_subgraphs.agents.analysis_agent import AnalysisAgent

def build_analysis_subgraph():
    """Build the analysis subgraph."""
    analysis_agent = AnalysisAgent()
    
    def analysis_node(state: MultiAgentState) -> MultiAgentState:
        """Execute analysis phase."""
        if not state.research_results:
            state.error_messages.append("No research results available for analysis")
            return state
        
        # Create analysis task
        analysis_task = AgentTask(
            id="analysis_1",
            task_type=TaskType.ANALYSIS,
            content=state.original_query,
            status=TaskStatus.IN_PROGRESS
        )
        
        # Process the task with research results
        completed_task = analysis_agent.process_task(analysis_task, state.research_results)
        
        # Update state
        state.tasks.append(completed_task)
        if completed_task.status == TaskStatus.COMPLETED:
            state.analysis_results = completed_task.result.split('\n\n')
            state.completed_phases.append(TaskType.ANALYSIS)
            state.current_phase = TaskType.SYNTHESIS
        else:
            state.error_messages.append(f"Analysis failed: {completed_task.result}")
        
        return state
    
    workflow = StateGraph(MultiAgentState)
    workflow.add_node("analysis", analysis_node)
    workflow.add_edge(START, "analysis")
    workflow.add_edge("analysis", END)
    
    return workflow.compile()