from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from part_09_web_api_integration.agents.web_agent import WebIntegrationAgent

class WebIntegrationState(TypedDict, total=False):
    input: str
    wikipedia: str
    duckduckgo: str
    output: str

def build_web_integration_graph():
    agent = WebIntegrationAgent()

    def web_node(state: WebIntegrationState) -> WebIntegrationState:
        query = state["input"]
        results = agent.run_with_web_context(query)
        return {
            "wikipedia": results["wikipedia"],
            "duckduckgo": results["duckduckgo"],
            "output": results["final_answer"]
        }

    workflow: StateGraph = StateGraph(WebIntegrationState)
    workflow.add_node("web_node", web_node)
    workflow.add_edge(START, "web_node")
    workflow.add_edge("web_node", END)

    return workflow.compile()
