from part_07_human_interrupts.schemas.state_schemas import InterruptState
from part_07_human_interrupts.agents.interruptible_agent import InterruptibleAgent

def test_interruptible_agent_triggers():
    agent = InterruptibleAgent("TestAgent")
    state = InterruptState(input="Please approve payment of $1000")
    updated_state = agent.run_with_interrupts(state)

    assert updated_state.awaiting_human is True
    assert "[HUMAN APPROVAL REQUIRED]" in updated_state.output

def test_interruptible_agent_normal():
    agent = InterruptibleAgent("TestAgent")
    state = InterruptState(input="Hello, how are you?")
    updated_state = agent.run_with_interrupts(state)

    assert updated_state.awaiting_human is False
    assert isinstance(updated_state.output, str)
