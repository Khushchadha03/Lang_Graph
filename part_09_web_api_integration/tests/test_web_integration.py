from part_09_web_api_integration.agents.web_agent import WebIntegrationAgent

def test_web_agent_basic():
    agent = WebIntegrationAgent()
    response = agent.run_with_web_context("Python (programming language)")
    assert isinstance(response, str)
    assert "Python" in response
