# part_07_human_interrupts/app.py

from shared.utils.azure_openai import run_llm_with_system


class HumanInLoopAgent:
    def __init__(self):
        self.history = []

    def run(self, user_input: str):
        """
        Run the agent with human interrupt handling.
        Returns a dict so we can distinguish between normal replies and interrupt cases.
        """

        # --- Step 1: Check for sensitive actions ---
        if "approve payment" in user_input.lower():
            return {
                "interrupt": True,
                "suggestion": "Sure, I will process payment of $1000."
            }

        if "delete file" in user_input.lower():
            return {
                "interrupt": True,
                "suggestion": "Okay, I will delete the requested file."
            }

        if "send email" in user_input.lower():
            return {
                "interrupt": True,
                "suggestion": "I will send the email as drafted."
            }

        # --- Step 2: Normal LLM handling ---
        reply = run_llm_with_system(
            "You are a helpful assistant. Pause for human approval on sensitive actions.",
            user_input
        )
        self.history.append({"user": user_input, "agent": reply})
        return {"interrupt": False, "response": reply}


def main():
    print("Interruptible Agent ready! Type 'exit' to quit.")
    print("Agent may pause for human approval if sensitive actions are detected.")

    agent = HumanInLoopAgent()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        result = agent.run(user_input)

        # --- Step 3: Handle interrupt case ---
        if result["interrupt"]:
            print(f"Agent: [HUMAN APPROVAL REQUIRED] Suggested response: {result['suggestion']}")
            human_input = input("⚠️ Human needed! Enter feedback or 'approve': ")
            agent.history.append({"human": human_input})
            print("✅ Human input recorded. Continuing...")

        else:
            print(f"Agent: {result['response']}")


if __name__ == "__main__":
    main()
