import sys
from part_09_web_api_integration.graphs.web_integration_graph import build_web_integration_graph

def main():
    workflow = build_web_integration_graph()
    print("Web API Integration Agent ready! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            sys.exit(0)

        state = {"input": user_input}
        result = workflow.invoke(state)

        print("\n--- Contexts ---")
        print(f"Wikipedia: {result['wikipedia']}")
        print(f"DuckDuckGo: {result['duckduckgo']}")
        print("\n--- Final Answer (GPT) ---")
        print(result["output"])
        print("\n")

if __name__ == "__main__":
    main()
