# Pilot

A harness for single and group of AI models and their replicas to perform a wide range of tasks, from coding and reasoning to more specialized operations.

## Installation

```sh
# Clone the repository
git clone https://github.com/AttAditya/pilot.git
cd pilot

# Source the development environment
source dev.sh

# Setup and run
dev setup
dev run
```

## About

Pilot is designed to be a flexible and extensible framework for orchestrating interactions between various AI models. It provides a structured way to define roles, contexts, and interactions, allowing developers to create complex workflows and applications with ease.

## Ecosystem Models

- Tili: Modified version of QWEN2.5:7B
  - Chat
  - Summarization
  - Planning
  - Code Generation

## Project Structure

```tree
pilot
├── __init__.py
├── __main__.py
├── data
│   ├── __init__.py
│   ├── content.py
│   ├── context.py
│   ├── control.py
│   └── figures.py
├── formatter
│   ├── __init__.py
│   ├── base.py
│   └── penguin.py
├── io
│   ├── __init__.py
│   ├── base.py
│   ├── console.py
│   └── pipe.py
├── role
│   ├── __init__.py
│   ├── base.py
│   ├── chat.py
│   ├── registry.py
│   └── user.py
└── tools
    ├── __init__.py
    └── base.py
```

### Module Overview

- `data`: managing the states of the Pilot ecosystem
- `formatter`: context and chat history formatting
- `io`: input and output management
- `role`: defining different roles in the ecosystem
- `tools`: tools accessible to the roles

## Ecosystem Philosophy

- Role Based: Each model, agent and role is defined as a "Role" with specific capabilities and responsibilities.
- Limited Context: Roles have access to limited context, encouraging more efficient and relevant interactions. Less dilution and more focus.
- Tool Usage: Roles can utilize tools to perform specific tasks, enhancing their capabilities and allowing for more complex interactions. Some roles exists specifically for tool usage and orchestration.

## Status

Experimental and under active development.  
APIs and structure may evolve as the project grows.

## Links

- [GitHub](https://github.com/attaditya/pilot)
- [License](https://github.com/attaditya/pilot/tree/main/LICENSE)

> _Made with <3 by [AttAditya](https://github.com/AttAditya)_
