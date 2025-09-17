from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from part_04_dynamic_router.agents.router_agent import RouterAgent

class RouterState(TypedDict, total=False):
    input: str
    output: str
    route: str

def build_router_graph():
    """Build a dynamic routing graph."""
    agent = RouterAgent(name="RouterAgent")

    def route_and_process(state: RouterState) -> RouterState:
        user_input: str = state["input"]
        output: str = agent.run_with_routing(user_input)
        return {"output": output}

    workflow: StateGraph = StateGraph(RouterState)
    workflow.add_node("route_and_process", route_and_process)
    workflow.add_edge(START, "route_and_process")
    workflow.add_edge("route_and_process", END)

    return workflow.compile()