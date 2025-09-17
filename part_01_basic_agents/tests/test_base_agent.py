from part_01_basic_agents.agents.base_agent import BaseAgent

def test_base_agent_runs() -> None:
    agent: BaseAgent = BaseAgent("TestAgent")
    output: str = agent.run("Hello, how are you?")
    assert isinstance(output, str)
    assert len(output) > 0