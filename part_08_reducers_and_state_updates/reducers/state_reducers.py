from typing import List, Dict, Any

class StateReducer:
    """Reducer to merge multiple agent outputs into a single state."""


    @staticmethod
    def combine_inputs(history: list, new_input: str) -> str:
        """Combine all past inputs into one string."""
        updated_history = history + [new_input]
        combined = " | ".join(updated_history)
        return combined


    @staticmethod
    def update_state(state: Dict[str, Any], new_outputs: List[str]) -> Dict[str, Any]:
        """Update conversation or task state with reduced output."""
        combined_output = StateReducer.combine_agent_outputs(new_outputs)
        state["output"] = combined_output
        if "history" in state:
            state["history"].append(combined_output)
        return state
