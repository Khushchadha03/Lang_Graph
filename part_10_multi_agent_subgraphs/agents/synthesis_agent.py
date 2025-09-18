from typing import List
from shared.utils.azure_openai import run_llm_with_system
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, AgentTask, TaskType, TaskStatus

class SynthesisAgent:
    """Specialized agent for synthesizing information from multiple sources."""
    
    def __init__(self, name: str = "SynthesisAgent"):
        self.name = name
        self.specialization = "information synthesis and comprehensive reporting"
    
    def synthesize_findings(self, research_results: List[str], analysis_results: List[str], original_query: str) -> str:
        """Synthesize research and analysis into a comprehensive response."""
        
        combined_research = "\n\n".join(research_results)
        combined_analysis = "\n\n".join(analysis_results)
        
        system_prompt = f"""You are {self.name}, specialized in {self.specialization}.

Create a comprehensive, well-structured response that synthesizes all the information below.
Your response should:
1. Directly answer the original query
2. Integrate key research findings
3. Include analytical insights
4. Provide a clear conclusion

Research Findings:
{combined_research}

Analysis Results:
{combined_analysis}

Original Query: {original_query}"""

        response = run_llm_with_system(system_prompt, "Synthesize all information into a comprehensive response.")
        return response
    
    def process_task(self, task: AgentTask, research_results: List[str], analysis_results: List[str]) -> AgentTask:
        """Process a synthesis task."""
        try:
            synthesis_result = self.synthesize_findings(research_results, analysis_results, task.content)
            task.result = synthesis_result
            task.status = TaskStatus.COMPLETED
            task.metadata["synthesized_sources"] = len(research_results) + len(analysis_results)
        except Exception as e:
            task.status = TaskStatus.FAILED
            task.result = f"Synthesis failed: {str(e)}"
        
        return task