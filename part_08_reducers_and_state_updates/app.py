import sys
from part_08_reducers_and_state_updates.graphs.reducer_graph import build_reducer_graph

def main():
    workflow = build_reducer_graph()
    print("Reducer Agent ready! Type 'exit' to quit.")

    # Initialize state
    state = {"input": "", "history": [], "output": ""}

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            sys.exit(0)

        state["input"] = user_input

        # Pass state through the graph
        state = workflow.invoke(state)

        print(f"Reducer Output: {state['output']}")

if __name__ == "__main__":
    main()
