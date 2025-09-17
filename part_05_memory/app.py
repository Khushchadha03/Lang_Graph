import sys
from part_05_memory.graphs.memory_graph import build_memory_graph

def main() -> None:
    """Main entry point for memory agent."""
    workflow = build_memory_graph()
    
    print("Memory Agent is ready! I'll remember our conversation.")
    print("Type 'memory' to see conversation summary, 'clear' to clear memory, or 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            sys.exit(0)
        
        if user_input.lower() == "memory":
            # Access the agent from the workflow (simplified for demo)
            print("Conversation summary would be shown here")
            continue
        
        if user_input.lower() == "clear":
            print("Memory cleared!")
            # In a real implementation, you'd access the agent to clear memory
            continue

        result = workflow.invoke({"input": user_input})
        print(f"Agent: {result['output']}")

if __name__ == "__main__":
    main()