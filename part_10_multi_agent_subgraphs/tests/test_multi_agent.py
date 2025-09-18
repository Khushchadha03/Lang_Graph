import pytest
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, TaskType, AgentTask
from part_10_multi_agent_subgraphs.agents.research_agent import ResearchAgent
from part_10_multi_agent_subgraphs.agents.analysis_agent import AnalysisAgent
from part_10_multi_agent_subgraphs.agents.synthesis_agent import SynthesisAgent
from part_10_multi_agent_subgraphs.coordinators.agent_coordinator import AgentCoordinator

def test_research_agent():
    """Test research agent functionality."""
    agent = ResearchAgent()
    results = agent.conduct_research("What is artificial intelligence?")
    assert isinstance(results, list)
    assert len(results) > 0
    assert all(isinstance(result, str) for result in results)

def test_analysis_agent():
    """Test analysis agent functionality."""
    agent = AnalysisAgent()
    research_data = ["AI is machine intelligence", "AI has many applications"]
    results = agent.analyze_research(research_data, "What is AI?")
    assert isinstance(results, list)
    assert len(results) > 0

def test_synthesis_agent():
    """Test synthesis agent functionality."""
    agent = SynthesisAgent()
    research_results = ["AI definition here"]
    analysis_results = ["AI analysis here"]
    result = agent.synthesize_findings(research_results, analysis_results, "What is AI?")
    assert isinstance(result, str)
    assert len(result) > 0

def test_agent_coordinator():
    """Test agent coordinator functionality."""
    coordinator = AgentCoordinator()
    state = MultiAgentState(
        original_query="Test query",
        research_results=["result1"],
        completed_phases=[TaskType.RESEARCH]
    )
    
    should_proceed = coordinator.should_proceed_to_next_phase(state, TaskType.RESEARCH)
    assert should_proceed == True
    
    summary = coordinator.get_execution_summary(state)
    assert isinstance(summary, dict)
    assert "query" in summary
    assert "phases_completed" in summary

def test_multi_agent_state():
    """Test multi-agent state schema."""
    state = MultiAgentState(original_query="Test query")
    assert state.original_query == "Test query"
    assert state.current_phase == TaskType.RESEARCH
    assert len(state.tasks) == 0
    assert len(state.research_results) == 0
    
    # Test adding a task
    task = AgentTask(id="test", task_type=TaskType.RESEARCH, content="test content")
    state.tasks.append(task)
    assert len(state.tasks) == 1