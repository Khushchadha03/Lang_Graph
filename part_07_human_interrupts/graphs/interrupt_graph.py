from langgraph.graph import StateGraph, START, END
from part_07_human_interrupts.agents.interruptible_agent import InterruptibleAgent
from part_07_human_interrupts.schemas.state_schemas import InterruptState

def build_interrupt_graph():
    agent = InterruptibleAgent("InterruptibleAgent")

    def process_with_interrupts(state: InterruptState) -> InterruptState:
        return agent.run_with_interrupts(state)

    workflow: StateGraph = StateGraph(InterruptState)
    workflow.add_node("process_with_interrupts", process_with_interrupts)
    workflow.add_edge(START, "process_with_interrupts")
    workflow.add_edge("process_with_interrupts", END)

    return workflow.compile()
