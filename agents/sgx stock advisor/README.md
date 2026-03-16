# SGX Stock Advisor: Agentic Workflow Framework

## Introduction
Welcome to the SGX Stock Advisor project. This repository contains the configuration and logic required to run a multi-specialist agentic workflow on Claude. The system analyzes Singapore Exchange (SGX) stocks by balancing dividend yields, growth potential, and macro-economic factors.

## 🏗️ 1. Project Architecture
We use a 4-layer hierarchical design to ensure the LLM operates with precision:

- **Agent (Orchestrator)**: sgx_stock_advisor — Defines the intent and manages the specialist pipeline.
- **Specialists**: Dedicated profiles for Dividend, Growth, Macro, and Synthesis.
  - growth_potential_analyst.md
  - macro_strategeist.md
  - sgx_analyst.md
  - synthesizer.md
- **Skills**: Technical tools (MCP/Python) and instruction-based soft skills.
  - growth_evaluation.md
  - macro_research.md
  - synthesis.md
  - API server - market_intelligence_skill.py
- **Guardrails**: Safety and compliance rules for financial analysis.
  - sgx_stock_advisor_guardrails.md

## 🚀 2. Implementation Steps (for Claude Projects)
To run this workflow in Claude, follow these steps to populate your Project Knowledge and Custom Instructions.

### 📁 Step A: Upload Knowledge Files
Upload the following files to the "Project Knowledge" section of your Claude Project:

**Specialists**:
- sgx_analyst.md (Dividend expert)
- growth_evaluation.md (Growth & valuation expert)
- macro_strategist.md (Geo-politics & economy expert)
- synthesizer.md (Final report aggregator)

**Skills**:
- macro_research_skill.md (Web search/data logic)
- growth_evaluation_skill.md (Logic for fundamental analysis)

**Guardrails**:
- sgx_stock_advisor_guardrails.md

### ⚙️ Step B: Configure Project Instructions
Copy and paste the content in sgx_stock_advisor.md into the "Custom Instructions" box of your Claude Project. This defines the Layer 1 (Agent) behavior.

### 🧰 Step C: Set up the API Server
In this example, we will set up a local MCP Server to run market_intelligence_skill.py to listen for requests from Claude Desktop.

Using `uv`:

1. Step - Open up Claude Desktop App and add the following into the claude_desktop_config.json
```commandline
"mcpServers": {
    "sgx_service": {
      "command": "uv",
      "args": [
        "--directory",
        "Path\\to\\parent\\folder",
        "run",
        "main.py"
      ]
    }
  }
```
2. Restart Claude App
3. Run the api server
`uv run script.py`

## 🛠️ 3. Detailed Component Breakdown
### 📊 Layer 2 & 3: Specialists & Skills
| Role             | Primary Skill        | Output Contribution                   |
|:-----------------|:---------------------|:--------------------------------------|
| SGX Analyst      | dividend_skill.py    | Yield, Payout Ratio, Sustainability.  |
| Growth Analyst   | growth_evaluation.md | Revenue trends, P/E ratios, Moat analysis. |
| Macro Strategist | macro_research.md    | Interest rate impact (MAS), Trade tensions. |
| Synthesizer      | 	synthesis_logic.md  | Final weighted score and Executive Summary.|

### 🛡️ Layer 4: Guardrails (Financial Baseline)
- **No Financial Advice**: Always include the disclaimer: "This is not financial advice. Please consult a MAS-licensed advisor."
- **Anti-Gambling**: Do not analyze speculative "Penny Stocks" with a market cap below $50M SGD.
- **Data Recency**: Always state the date of the last data point retrieved.

## 📝 4. Example Prompt to Run the Workflow
Once the files are uploaded and instructions are set, simply type the following in the project chat:

User: 
> "Analyze the following companies for me. I want to know if it's a good buy given the current high-interest-rate environment."
> 1. D05
> 2. O39
> 3. U11
> 4. AIY

The Agent will then:

1. Initialize the sgx_stock_advisor persona.
2. Sequential call to sgx_analyst for dividend data.
3. Consult growth_evaluation for banking sector upside.
4. Apply macro_strategist view on Fed rate pivots.
5. Output the final report via synthesizer.
