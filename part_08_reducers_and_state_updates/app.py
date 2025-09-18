import sys

def main():
    print("Reducer Agent ready! Type 'exit' to quit.")

    # Keep track of all past inputs
    state = {"history": [], "output": ""}

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            sys.exit(0)

        # Add new input to history
        state["history"].append(user_input)

        # Combine all inputs into a single reduced output
        state["output"] = " | ".join(state["history"])

        print(f"Reducer Output: {state['output']}")

if __name__ == "__main__":
    main()
