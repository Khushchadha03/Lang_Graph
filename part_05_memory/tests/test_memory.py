from part_05_memory.agents.memory_agent import MemoryAgent

def test_memory_agent():
    agent = MemoryAgent("TestMemory")
    
    # First interaction
    response1 = agent.run_with_memory("My name is John")
    assert isinstance(response1, str)
    assert len(response1) > 0
    
    # Second interaction should reference first
    response2 = agent.run_with_memory("What's my name?")
    assert isinstance(response2, str)
    assert len(response2) > 0
    # Check if "John" is mentioned in the reply (memory recall)
    assert "John" in response2 or "john" in response2
    
    # Test memory summary
    summary = agent.get_memory_summary()
    assert isinstance(summary, str)
    assert "messages exchanged" in summary
    
    # Clear memory and confirm
    agent.clear_memory()
    summary_after_clear = agent.get_memory_summary()
    assert "No conversation history" in summary_after_clear
