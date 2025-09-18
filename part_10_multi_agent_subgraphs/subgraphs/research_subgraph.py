from langgraph.graph import StateGraph, START, END
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, AgentTask, TaskType, TaskStatus
from part_10_multi_agent_subgraphs.agents.research_agent import ResearchAgent

def build_research_subgraph():
    """Build the research subgraph."""
    research_agent = ResearchAgent()
    
    def research_node(state: MultiAgentState) -> MultiAgentState:
        """Execute research phase."""
        # Create research task
        research_task = AgentTask(
            id="research_1",
            task_type=TaskType.RESEARCH,
            content=state.original_query,
            status=TaskStatus.IN_PROGRESS
        )
        
        # Process the task
        completed_task = research_agent.process_task(research_task)
        
        # Update state
        state.tasks.append(completed_task)
        if completed_task.status == TaskStatus.COMPLETED:
            state.research_results = completed_task.result.split('\n\n')
            state.completed_phases.append(TaskType.RESEARCH)
            state.current_phase = TaskType.ANALYSIS
        else:
            state.error_messages.append(f"Research failed: {completed_task.result}")
        
        return state
    
    workflow = StateGraph(MultiAgentState)
    workflow.add_node("research", research_node)
    workflow.add_edge(START, "research")
    workflow.add_edge("research", END)
    
    return workflow.compile()