from langgraph.graph import StateGraph, START, END
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, TaskType
from part_10_multi_agent_subgraphs.subgraphs.research_subgraph import build_research_subgraph
from part_10_multi_agent_subgraphs.subgraphs.analysis_subgraph import build_analysis_subgraph
from part_10_multi_agent_subgraphs.subgraphs.synthesis_subgraph import build_synthesis_subgraph
from part_10_multi_agent_subgraphs.coordinators.agent_coordinator import AgentCoordinator

def safe_invoke(graph, state: MultiAgentState) -> MultiAgentState:
    """Invoke a graph and ensure the result is MultiAgentState."""
    result = graph.invoke(state)
    if isinstance(result, dict):
        return MultiAgentState.parse_obj(result)
    return result

def build_master_graph():
    """Build the master graph that orchestrates all subgraphs."""
    
    # Build subgraphs
    research_graph = build_research_subgraph()
    analysis_graph = build_analysis_subgraph()
    synthesis_graph = build_synthesis_subgraph()
    
    coordinator = AgentCoordinator()
    
    def research_phase(state: MultiAgentState) -> MultiAgentState:
        """Execute research subgraph."""
        return safe_invoke(research_graph, state)
    
    def analysis_phase(state: MultiAgentState) -> MultiAgentState:
        """Execute analysis subgraph."""
        return safe_invoke(analysis_graph, state)
    
    def synthesis_phase(state: MultiAgentState) -> MultiAgentState:
        """Execute synthesis subgraph."""
        return safe_invoke(synthesis_graph, state)
    
    def route_after_research(state: MultiAgentState) -> str:
        if coordinator.should_proceed_to_next_phase(state, TaskType.RESEARCH):
            return "analysis"
        else:
            return "end"
    
    def route_after_analysis(state: MultiAgentState) -> str:
        if coordinator.should_proceed_to_next_phase(state, TaskType.ANALYSIS):
            return "synthesis"
        else:
            return "end"
    
    # Build master workflow
    workflow = StateGraph(MultiAgentState)
    
    workflow.add_node("research", research_phase)
    workflow.add_node("analysis", analysis_phase)  
    workflow.add_node("synthesis", synthesis_phase)
    
    workflow.add_edge(START, "research")
    workflow.add_conditional_edges("research", route_after_research, {"analysis": "analysis", "end": END})
    workflow.add_conditional_edges("analysis", route_after_analysis, {"synthesis": "synthesis", "end": END})
    workflow.add_edge("synthesis", END)
    
    return workflow.compile()
