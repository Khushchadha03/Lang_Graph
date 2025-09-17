import sys
from part_02_tool_calling.graphs.tool_graph import build_tool_graph

def main() -> None:
    """Main entry point for tool agent."""
    workflow = build_tool_graph()
    
    print("Tool Agent is ready! Available tools: calculator, text_analyzer, string_transformer, random_number_generator, word_counter")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            sys.exit(0)

        # Simple tool detection
        tool_name = None
        if any(word in user_input.lower() for word in ["calculate", "math", "+", "-", "*", "/"]):
            tool_name = "calculator"
        elif any(word in user_input.lower() for word in ["analyze", "analysis"]):
            tool_name = "text_analyzer"
        elif any(word in user_input.lower() for word in ["random", "number"]):
            tool_name = "random_number_generator"
        elif any(word in user_input.lower() for word in ["count", "words"]):
            tool_name = "word_counter"

        result = workflow.invoke({"input": user_input, "tool_name": tool_name})
        print(f"Agent: {result['output']}")

if __name__ == "__main__":
    main()