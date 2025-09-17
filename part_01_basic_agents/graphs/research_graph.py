from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from part_01_basic_agents.agents.base_agent import BaseAgent

class GraphState(TypedDict, total=False):
    """Defines the state passed between LangGraph nodes."""
    input: str
    output: str

def build_research_graph():
    """Build a basic research graph."""
    agent: BaseAgent = BaseAgent(name="ResearchAgent")

    def call_agent(state: GraphState) -> GraphState:
        user_input: str = state["input"]
        output: str = agent.run(user_input)
        return {"output": output}

    workflow: StateGraph = StateGraph(GraphState)
    workflow.add_node("agent_step", call_agent)
    workflow.add_edge(START, "agent_step")
    workflow.add_edge("agent_step", END)

    return workflow.compile()