from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from part_08_reducers_and_state_updates.reducers.state_reducers import StateReducer

class ReducerState(TypedDict, total=False):
    input: str
    intermediate_outputs: list
    output: str
    history: list

def build_reducer_graph():
    """Graph that reduces multiple agent outputs into a single state."""
    
    def reducer_node(state: ReducerState) -> ReducerState:
        outputs: list = state.get("intermediate_outputs", [])
        updated_state = StateReducer.update_state(state, outputs)
        return updated_state

    workflow: StateGraph = StateGraph(ReducerState)
    workflow.add_node("reduce_outputs", reducer_node)
    workflow.add_edge(START, "reduce_outputs")
    workflow.add_edge("reduce_outputs", END)

    return workflow.compile()
