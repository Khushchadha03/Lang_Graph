# LangGraph Multi-Agent System

A **modular, stateful multi-agent AI system** built with **LangGraph**, Azure OpenAI, and external APIs.  
The system supports **stateful conversations**, **human-in-the-loop interrupts**, **reducers**, **web context integration**, and **multi-agent orchestration**.

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Setup & Installation](#setup--installation)  
5. [Usage](#usage)  
6. [Testing](#testing)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## Overview

This project demonstrates a **scalable multi-agent architecture** using Python and LangGraph. The system evolves through the following stages:

- **Part 1–6:** Stateful agents with conversation memory  
- **Part 7:** Human-in-the-loop handling for sensitive actions  
- **Part 8:** Reducers to merge multiple outputs  
- **Part 9:** Web integration via Wikipedia and DuckDuckGo  
- **Part 10:** Multi-agent subgraphs: Research → Analysis → Synthesis  

The agents communicate via **typed state objects**, ensuring safe, structured information flow.

---

## Features

- **Stateful Agents:** Maintain conversation history and topics.  
- **Human Interrupts:** Pause agent responses for human approval on sensitive actions.  
- **Reducers:** Merge multiple outputs into a single coherent state.  
- **Web Context Integration:** Fetch summaries from Wikipedia and DuckDuckGo for informed responses.  
- **Multi-Agent Subgraphs:** Specialized agents for research, analysis, and synthesis.  
- **Coordinator:** Ensures correct phase execution and monitors state.  
- **Extensible Architecture:** Easy to add new agents, APIs, or subgraphs.

---

## Project Structure

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
│ ├── agents/
│ ├── schemas/
│ ├── graphs/
│ └── tests/
├── part_08_reducers_and_state_updates/
│ ├── reducers/
│ ├── graphs/
│ └── tests/
├── part_09_web_api_integration/
│ ├── agents/
│ ├── services/
│ ├── graphs/
│ └── tests/
├── part_10_multi_agent_subgraphs/
│ ├── agents/
│ ├── schemas/
│ ├── subgraphs/
│ ├── graphs/
│ ├── coordinators/
│ └── tests/
├── shared/
│ └── utils/
├── app.py # Main entry point for multi-agent system
└── README.md
│
└── shared/
    ├── __init__.py
    ├── configs/azure_config.py
    └── utils/azure_openai.py





---

## Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/langgraph-multi-agent.git
cd langgraph-multi-agent


python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt

export AZURE_OPENAI_KEY="your_key_here"
export AZURE_OPENAI_ENDPOINT="your_endpoint_here"

cd part_07_human_interrupts
python app.py
cd part_08_reducers_and_state_updates
python app.py
cd part_09_web_api_integration
python app.py
python app.py
You: Explain quantum computing
🔄 Processing through multi-agent pipeline...
✅ Completed 3/3 phases

🎯 Multi-Agent Response:
==================================================
Quantum computing is...
==================================================

pytest part_07_human_interrupts/tests/
pytest part_08_reducers_and_state_updates/tests/
pytest part_09_web_api_integration/tests/
pytest part_10_multi_agent_subgraphs/tests/

Contributing

Fork the repository
Create a feature branch (git checkout -b feature/new-agent)
Commit your changes (git commit -m 'Add new agent')
Push to the branch (git push origin feature/new-agent)
Open a Pull Request




License
---

If you want, I can **also make a super clean README with a diagram of the multi-agent workflow** included **as ASCII or Mermaid diagram** so it’s visually easier to understand—all in this same file.  

Do you want me to do that next?
