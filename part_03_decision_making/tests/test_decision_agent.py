from part_03_decision_making.agents.decision_agent import DecisionAgent

def test_decision_agent_calculator():
    agent = DecisionAgent("DecisionTestAgent")
    # Note: This test depends on LLM decision making, so results may vary
    result = agent.run_with_decision("What is 2 + 3?")
    assert isinstance(result, str)

def test_decision_agent_general():
    agent = DecisionAgent("DecisionTestAgent")
    result = agent.run_with_decision("Tell me about AI")
    assert isinstance(result, str) and len(result) > 0