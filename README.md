# Customer Support AI Agent

## Project Overview

This project aims to build an AI-powered customer support agent using Python, LangChain, and locally running LLMs through Ollama.

The goal is to develop an agent that can understand customer queries, identify user intent, and route requests to appropriate workflows. The project is being developed incrementally, starting with basic LLM interaction and moving toward more advanced agentic workflows.

## Current Features

- Accepts customer queries through a simple Python interface.
- Generates responses using a locally running LLM via Ollama.
- Classifies customer queries into intents.
- Uses LangGraph to structure the workflow and manage query processing.

## Tech Stack

- **Language:** Python
- **LLM Framework:** LangChain
- **Local LLM Runtime:** Ollama
- **Workflow Orchestration:** LangGraph
- **Version Control:** Git and GitHub

## Project Structure

```text
Customer_Support_Agent/
├── app/
│   ├── __init__.py
│   ├── customer.py
│   ├── graph.py
│   ├── llm.py
│   ├── main.py
│   ├── nodes.py
│   └── state.py
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Customer_Support_Agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install the required packages used by the project:

```bash
pip install langchain langchain-ollama langgraph
```

### 4. Set up Ollama

Install Ollama and download a compatible model. For example, if you plan to use `qwen3:4b-instruct`, verify that this exact model tag is available in your Ollama installation.

```bash
ollama pull qwen3:4b-instruct
```

Ensure Ollama is running before executing the application.

### 5. Run the application

From the project root:

```bash
python -m app.main
```

## Development Roadmap

- [x] Basic LLM interaction
- [x] Initial intent classification
- [x] Initial LangGraph workflow structure
- [ ] Intent-based query routing
- [ ] Tool integration
- [ ] Human escalation workflow
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Automated testing
- [ ] CI/CD using GitHub Actions
- [ ] Deployment

## Future Improvements

The project will be improved incrementally with a focus on reliable query handling, modular code, automated testing, and deployment practices.

## Note

This project is under active development. Features and workflows may change as new capabilities are added.
