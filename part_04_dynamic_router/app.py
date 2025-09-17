import sys
from part_04_dynamic_router.graphs.router_graph import build_router_graph

def main() -> None:
    """Main entry point for router agent."""
    workflow = build_router_graph()
    
    print("Dynamic Router Agent is ready!")
    print("I can route to specialists: math, text, research, creative, tools")
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