from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from part_05_memory.agents.memory_agent import MemoryAgent

class MemoryState(TypedDict, total=False):
    input: str
    output: str

def build_memory_graph():
    """Build a memory-enabled graph."""
    agent = MemoryAgent(name="MemoryAgent")

    def process_with_memory(state: MemoryState) -> MemoryState:
        user_input: str = state["input"]
        output: str = agent.run_with_memory(user_input)
        return {"output": output}

    workflow: StateGraph = StateGraph(MemoryState)
    workflow.add_node("process_with_memory", process_with_memory)
    workflow.add_edge(START, "process_with_memory")
    workflow.add_edge("process_with_memory", END)

    return workflow.compile()