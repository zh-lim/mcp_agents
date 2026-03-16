# MCP Agents

Agentic workflows imagined in a microservices manners (skills)

## 🏗️ The 4-Layer Abstraction Framework
This project follows a structured hierarchy to ensure modularity, scalability, and safety.

**Layer 1: Agents (The Orchestrators) 🧠**
- Definition: Defines the high-level intent and manages the "Runbook."
- Role: Acts as the project manager, delegating tasks to specialists.

**Layer 2: Specialists (The Experts) 🧑‍🔬**
- Definition: Domain-specific personas with focused logic.
- Role: Performs a specified set of tasks and provides a focused output.

**Layer 3: Skills (The Capabilities) 🛠️**
- Definition: Atomic actions. Can be Hard Skills (Python/API via MCP) or Soft Skills (Markdown reasoning).

**Layer 4: Guardrails (The Boundaries) 🛡️**
- Definition: Sets the baseline for `dos and don'ts`, Ethical and operational constraints.

## 🚀 Implementation Guide
### 1. Setting up the MCP Server (Skills)
To enable the Hard Skills, you must run the MCP server.

   - Ensure you have uv or pip installed.
   - Run the service
    ```commandline
    uv run /path/to/script/main.py
    ```
   - Add the server to your Claude Desktop configuration (claude_desktop_config.json)

### 2. Configuring Claude Projects
To run the workflow in Claude:

1. Create a New Project
2. Upload Context Files: Upload all .md files from the specialists, skills, and guardrails folders into the Project Knowledge.
3. Set Custom Instructions: Copy the content of agents/<agent_orchestrator>.md into the Project's "Custom Instructions."

