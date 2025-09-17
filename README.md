langgraph-complete-learning/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── part_01_basic_agents/
│   ├── app.py
│   ├── configs/azure_config.py
│   ├── agents/base_agent.py
│   ├── graphs/research_graph.py
│   ├── utils/azure_openai.py
│   └── tests/test_base_agent.py
│
├── part_02_tool_calling/
│   ├── app.py
│   ├── agents/tool_agent.py
│   ├── graphs/tool_graph.py
│   ├── utils/tools.py
│   └── tests/test_tool_agent.py
│
├── part_03_decision_making/
│   ├── app.py
│   ├── agents/decision_agent.py
│   ├── graphs/decision_graph.py
│   └── tests/test_decision_agent.py
│
├── part_04_dynamic_router/
│   ├── app.py
│   ├── agents/router_agent.py
│   ├── graphs/router_graph.py
│   ├── routers/dynamic_router.py
│   └── tests/test_router.py
│
├── part_05_memory/
│   ├── app.py
│   ├── agents/memory_agent.py
│   ├── graphs/memory_graph.py
│   ├── memory/conversation_memory.py
│   └── tests/test_memory.py
│
├── part_06_state_management/
│   ├── app.py
│   ├── schemas/state_schemas.py
│   ├── agents/stateful_agent.py
│   ├── graphs/stateful_graph.py
│   └── tests/test_state_management.py
│
├── part_07_human_interrupts/
│   ├── app.py
│   ├── agents/interactive_agent.py
│   ├── graphs/interactive_graph.py
│   ├── interrupts/human_interrupt.py
│   └── tests/test_interrupts.py
│
├── part_08_reducers/
│   ├── app.py
│   ├── reducers/state_reducers.py
│   ├── graphs/reducer_graph.py
│   └── tests/test_reducers.py
│
├── part_09_web_api_integration/
│   ├── app.py
│   ├── connectors/api_connectors.py
│   ├── agents/web_agent.py
│   ├── graphs/web_graph.py
│   └── tests/test_web_integration.py
│
├── part_10_multi_agent_subgraphs/
│   ├── app.py
│   ├── subgraphs/research_subgraph.py
│   ├── subgraphs/analysis_subgraph.py
│   ├── graphs/master_graph.py
│   ├── coordinators/agent_coordinator.py
│   └── tests/test_multi_agent.py
│
└── shared/
    ├── __init__.py
    ├── configs/azure_config.py
    └── utils/azure_openai.py