import sys
from part_06_state_management.graphs.stateful_graph import build_stateful_graph
from part_06_state_management.schemas.state_schemas import ConversationState

def main() -> None:
    """Main entry point for stateful agent."""
    workflow = build_stateful_graph()
    
    print("Stateful Agent is ready! I manage structured state like history and topics.")
    print("Type 'exit' to quit or 'state' to see current structured state.")

    state = ConversationState(input="", history=[], topic=None)

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            sys.exit(0)

        if user_input.lower() == "state":
            print("--- Current State ---")
            print(f"Topic: {state.topic}")
            print(f"History (last 5): {state.history[-5:]}")
            continue

        state.input = user_input
        result = workflow.invoke(state)
        # Coerce back into ConversationState
        if isinstance(result, dict):
            state = ConversationState(**result)
        else:
            state = result
        print(f"Agent: {state.output}")


if __name__ == "__main__":
    main()
