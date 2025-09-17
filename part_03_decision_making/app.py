import sys
from part_03_decision_making.graphs.decision_graph import build_decision_graph

def main() -> None:
    """Main entry point for decision agent."""
    workflow = build_decision_graph()
    
    print("Decision Agent is ready! I can automatically choose the right tool for your task.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            sys.exit(0)

        result = workflow.invoke({"input": user_input})
        print(f"Agent: {result['output']}")

if __name__ == "__main__":
    main()