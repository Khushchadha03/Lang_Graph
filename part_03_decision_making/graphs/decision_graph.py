from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from part_03_decision_making.agents.decision_agent import DecisionAgent

class DecisionGraphState(TypedDict, total=False):
    input: str
    output: str

def build_decision_graph():
    """Build a decision-making graph."""
    agent: DecisionAgent = DecisionAgent(name="DecisionAgent")

    def agent_step(state: DecisionGraphState) -> DecisionGraphState:
        user_input: str = state["input"]
        output: str = agent.run_with_decision(user_input)
        return {"output": output}

    workflow: StateGraph = StateGraph(DecisionGraphState)
    workflow.add_node("agent_step", agent_step)
    workflow.add_edge(START, "agent_step")
    workflow.add_edge("agent_step", END)

    return workflow.compile()