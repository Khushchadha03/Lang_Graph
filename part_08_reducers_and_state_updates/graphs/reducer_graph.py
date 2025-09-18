from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from part_08_reducers_and_state_updates.reducers.state_reducers import StateReducer

class ReducerState(TypedDict, total=False):
    input: str
    history: list
    output: str

def build_reducer_graph():
    """Graph that accumulates inputs and reduces them into a single string."""

    def reducer_node(state: ReducerState) -> ReducerState:
        new_state = StateReducer.combine_inputs(
            state.get("history", []),
            state["input"]
        )
        return {**state, **new_state}

    workflow: StateGraph = StateGraph(ReducerState)
    workflow.add_node("reduce_inputs", reducer_node)
    workflow.add_edge(START, "reduce_inputs")
    workflow.add_edge("reduce_inputs", END)

    return workflow.compile()
