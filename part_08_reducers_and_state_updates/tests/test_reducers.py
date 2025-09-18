from part_08_reducers_and_state_updates.reducers.state_reducers import StateReducer

def test_combine_agent_outputs():
    outputs = ["Hello", "World"]
    combined = StateReducer.combine_agent_outputs(outputs)
    assert "Hello" in combined and "World" in combined

def test_update_state():
    state = {"output": "", "history": []}
    new_outputs = ["First", "Second"]
    updated = StateReducer.update_state(state, new_outputs)
    assert updated["output"] == "First | Second"
    assert "First | Second" in updated["history"]
