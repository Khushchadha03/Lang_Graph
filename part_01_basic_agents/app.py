import sys
from part_01_basic_agents.graphs.research_graph import build_research_graph

def main() -> None:
    """Main entry point for basic agent."""
    workflow = build_research_graph()
    
    print("Basic Agent is ready! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            sys.exit(0)

        result = workflow.invoke({"input": user_input})
        print(f"Agent: {result['output']}")

if __name__ == "__main__":
    main()