from langgraph.graph import StateGraph, START, END
from part_06_state_management.agents.stateful_agent import StatefulAgent
from part_06_state_management.schemas.state_schemas import ConversationState

def build_stateful_graph():
    """Build a graph with structured state management."""
    agent = StatefulAgent(name="StatefulAgent")

    def process_with_state(state: ConversationState) -> ConversationState:
        return agent.run_with_state(state)

    workflow: StateGraph = StateGraph(ConversationState)
    workflow.add_node("process_with_state", process_with_state)
    workflow.add_edge(START, "process_with_state")
    workflow.add_edge("process_with_state", END)

    return workflow.compile()
