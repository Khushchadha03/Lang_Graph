from typing import List
from shared.utils.azure_openai import run_llm_with_system
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, AgentTask, TaskType, TaskStatus

class ResearchAgent:
    """Specialized agent for conducting research tasks."""
    
    def __init__(self, name: str = "ResearchAgent"):
        self.name = name
        self.specialization = "information gathering and fact finding"
    
    def conduct_research(self, query: str) -> List[str]:
        """Conduct research on a given query."""
        system_prompt = f"""You are {self.name}, specialized in {self.specialization}.
        
Your task is to research the given query thoroughly. Provide 3 distinct research findings:
1. Key facts and definitions
2. Current trends or developments  
3. Relevant background context

Format each finding as a separate, comprehensive paragraph."""

        response = run_llm_with_system(system_prompt, f"Research query: {query}")
        
        # Split response into research findings
        findings = [finding.strip() for finding in response.split('\n\n') if finding.strip()]
        return findings[:3] if len(findings) >= 3 else [response]
    
    def process_task(self, task: AgentTask) -> AgentTask:
        """Process a research task."""
        try:
            research_results = self.conduct_research(task.content)
            task.result = "\n\n".join(research_results)
            task.status = TaskStatus.COMPLETED
            task.metadata["findings_count"] = len(research_results)
        except Exception as e:
            task.status = TaskStatus.FAILED
            task.result = f"Research failed: {str(e)}"
        
        return task