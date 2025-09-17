from part_04_dynamic_router.agents.router_agent import RouterAgent

def test_router_agent():
    agent = RouterAgent("TestRouter")
    result = agent.run_with_routing("What is 2 + 2?")
    assert isinstance(result, str)
    assert "[" in result and "]" in result  # Check for specialist prefix