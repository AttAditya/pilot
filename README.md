<div align="center">

```txt
__|__
--o--(_)--o--
P I L O T
```

# Pilot

[![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpypi.org%2Fpypi%2Fpilot-code%2Fjson&query=info.version&prefix=v&style=for-the-badge&logo=pypi&logoColor=%23ffffff&label=PyPI%20Release&labelColor=%230073b7&color=%23ffffff&link=https%3A%2F%2Fpypi.org%2Fproject%2Fpilot-code%2F&cacheSeconds=30)](https://pypi.org/project/pilot-code/)
[![Sponsor](https://img.shields.io/badge/Sponsor%20PROJECT-db61a2?style=for-the-badge&logo=github)](https://github.com/sponsors/AttAditya)

A harness for single and group of AI models and their replicas to perform a wide range of tasks, from coding and reasoning to more specialized operations.

</div>

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
│   ├── figures.py
│   └── manager.py
├── formatter
│   ├── __init__.py
│   ├── base.py
│   └── penguin.py
├── io
│   ├── __init__.py
│   ├── base.py
│   ├── cli.py
│   └── console.py
└── role
    ├── __init__.py
    ├── base.py
    ├── registry.py
    └── user.py
```

### Module Overview

- `data`: managing the states of the Pilot ecosystem
- `formatter`: context and chat history formatting
- `io`: input and output management
- `role`: defining different roles in the ecosystem

## Ecosystem Philosophy

- Role Based: Each model, agent and role is defined as a "Role" with specific capabilities and responsibilities.
- Limited Context: Roles have access to limited context, encouraging more efficient and relevant interactions. Less dilution and more focus.
- Tool Usage: Roles can utilize tools to perform specific tasks, enhancing their capabilities and allowing for more complex interactions. Some roles exists specifically for tool usage and orchestration.

## Status

Experimental and under active development.  
APIs and structure may evolve as the project grows.

## Links

- [PyPI](https://pypi.org/project/pilot-code/)
- [GitHub](https://github.com/attaditya/pilot)
- [License](https://github.com/attaditya/pilot/tree/main/LICENSE)


## Contributors

<a href="https://github.com/attaditya/pilot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=attaditya/pilot" />
</a>

## Support

If you find this project useful, please consider supporting it by **starring the GitHub repository** or sharing it with others who might benefit from it.

Your support helps in the continued development and improvement of the project.

You can also **contribute to the project** by submitting issues, suggesting features, or even contributing code through pull requests.

You can also sponsor the project on GitHub Sponsors: [GitHub Sponsors - AttAditya](https://github.com/sponsors/AttAditya)

---

> ###### _Made with_ `<3` _by [AttAditya](https://github.com/AttAditya)_

