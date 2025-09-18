class StateReducer:
    @staticmethod
    def combine_inputs(history: list, new_input: str) -> dict:
        """Update state by combining all inputs into one reduced output."""
        updated_history = history + [new_input]
        combined = " | ".join(updated_history)
        return {"history": updated_history, "output": combined}
