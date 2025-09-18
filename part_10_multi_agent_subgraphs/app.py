import sys
from part_10_multi_agent_subgraphs.schemas.multi_agent_schemas import MultiAgentState, TaskType
from part_10_multi_agent_subgraphs.graphs.master_graph import build_master_graph, safe_invoke
from part_10_multi_agent_subgraphs.coordinators.agent_coordinator import AgentCoordinator

def main():
    """Main entry point for multi-agent system."""
    master_graph = build_master_graph()
    coordinator = AgentCoordinator()
    
    print("🤖 Multi-Agent System Ready!")
    print("This system uses 3 specialized agents:")
    print("  📚 Research Agent - Gathers information")
    print("  🔍 Analysis Agent - Analyzes findings") 
    print("  📝 Synthesis Agent - Creates comprehensive response")
    print("\nType 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            sys.exit(0)
        
        # Initialize state
        initial_state = MultiAgentState(
            original_query=user_input,
            current_phase=TaskType.RESEARCH
        )
        
        print("\n🔄 Processing through multi-agent pipeline...")
        
        try:
            # Execute the master graph safely
            final_state = safe_invoke(master_graph, initial_state)
            
            # Get execution summary
            summary = coordinator.get_execution_summary(final_state)
            
            print(f"\n✅ Completed {len(summary['phases_completed'])}/3 phases")
            
            if final_state.final_output:
                print(f"\n🎯 Multi-Agent Response:")
                print("=" * 50)
                print(final_state.final_output)
                print("=" * 50)
            else:
                print(f"\n❌ System encountered errors:")
                for error in final_state.error_messages:
                    print(f"  - {error}")
                    
        except Exception as e:
            print(f"\n💥 Multi-agent system error: {str(e)}")

if __name__ == "__main__":
    main()
