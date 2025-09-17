from part_06_state_management.schemas.state_schemas import ConversationState
from part_06_state_management.agents.stateful_agent import StatefulAgent

def test_stateful_agent():
    agent = StatefulAgent("TestStateful")
    state = ConversationState(input="Hello, my name is Alice")
    updated_state = agent.run_with_state(state)

    assert isinstance(updated_state.output, str)
    assert "Alice" in " ".join(updated_state.history) or "alice" in " ".join(updated_state.history)
    assert updated_state.topic is not None
