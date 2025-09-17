from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from part_02_tool_calling.agents.tool_agent import ToolAgent

class ToolGraphState(TypedDict, total=False):
    input: str
    output: str
    tool_name: str

def build_tool_graph():
    """Build a tool-calling graph."""
    agent = ToolAgent(name="ToolAgent")

    def agent_step(state: ToolGraphState) -> ToolGraphState:
        user_input: str = state["input"]
        tool_name: str = state.get("tool_name")
        output: str = agent.run_with_tools(user_input, tool_name)
        return {"output": output}

    workflow: StateGraph = StateGraph(ToolGraphState)
    workflow.add_node("agent_step", agent_step)
    workflow.add_edge(START, "agent_step")
    workflow.add_edge("agent_step", END)

    return workflow.compile()