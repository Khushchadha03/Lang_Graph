from typing import List
from shared.utils.azure_openai import run_llm_with_system
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, AgentTask, TaskType, TaskStatus

class AnalysisAgent:
    """Specialized agent for analyzing research data."""
    
    def __init__(self, name: str = "AnalysisAgent"):
        self.name = name
        self.specialization = "data analysis and pattern recognition"
    
    def analyze_research(self, research_data: List[str], original_query: str) -> List[str]:
        """Analyze research findings."""
        combined_research = "\n\n".join(research_data)
        
        system_prompt = f"""You are {self.name}, specialized in {self.specialization}.

Analyze the research findings below in relation to the original query. Provide 2 distinct analyses:
1. Key insights and patterns identified
2. Implications and significance of the findings

Research Data:
{combined_research}

Original Query: {original_query}"""

        response = run_llm_with_system(system_prompt, "Perform detailed analysis.")
        
        # Split into analysis components
        analyses = [analysis.strip() for analysis in response.split('\n\n') if analysis.strip()]
        return analyses[:2] if len(analyses) >= 2 else [response]
    
    def process_task(self, task: AgentTask, research_results: List[str]) -> AgentTask:
        """Process an analysis task."""
        try:
            analysis_results = self.analyze_research(research_results, task.content)
            task.result = "\n\n".join(analysis_results)
            task.status = TaskStatus.COMPLETED
            task.metadata["analysis_components"] = len(analysis_results)
        except Exception as e:
            task.status = TaskStatus.FAILED
            task.result = f"Analysis failed: {str(e)}"
        
        return task