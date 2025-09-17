from part_02_tool_calling.agents.tool_agent import ToolAgent

def test_tool_agent_calculator():
    agent = ToolAgent("TestAgent")
    result = agent.run_with_tools("2 + 3", "calculator")
    assert result == "5"

def test_tool_agent_without_tool():
    agent = ToolAgent("TestAgent")
    result = agent.run_with_tools("Hello")
    assert isinstance(result, str)