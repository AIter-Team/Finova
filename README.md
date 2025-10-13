# Finova: Your Agentic Financial Assistant 

![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Google%20ADK-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Finova is an intelligent, agent-based financial assistant designed to help you manage your finances with unparalleled insight and autonomy. Orchestrated using Google's Agent Developer Kit (ADK), Finova provides a conversational and intuitive way to handle your financial life.

## ⚠️ Development Status

**This project is currently under active development.**

Please be aware that Finova is an experimental application. Features may change, and the current version is not recommended for managing real financial data. It is intended for demonstration and development purposes only. We welcome feedback and contributions as we continue to improve it!

## 📖 What is Finova?

Traditional finance apps often act as simple ledgers, requiring manual input and providing limited insight. Finova is different. It's built on a powerful **agentic architecture**, meaning it operates not as a single program, but as a team of specialist agents that collaborate to understand your needs and execute complex tasks.

## ✨ Core Features

* **Multi-Agent System:** Utilizes specialized agents for writing transactions, reading data, and providing financial advice for a robust and modular architecture.
* **Natural Language Interaction:** Simply talk to Finova as you would a human assistant.
* **Automated Transaction Logging:** Easily record income and expenses with tools that handle data formatting and database insertion.
* **Stateful Memory:** Finova remembers your name, balance, and financial goals across conversations for a personalized experience.
* **Database Integration:** Uses a local SQLite database to securely store and manage your transaction history.
* **Optional Observability:** Integrated with Langfuse to provide clear observability into agent performance and behavior for developers.

## 🔧 Getting Started

Follow these steps to get your own Finova instance running locally.

### Prerequisites

* **Python 3.13+**
* **uv** (can be installed via `pipx` or `pip`)
* A **Google API Key** for Gemini Models.

---

### For Standard Users

These instructions will get the application running without the development and observability tools.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/AIter-Team/Finova.git
    cd finova
    ```

2.  **Create and Sync the Environment:**
    * This command creates a virtual environment and installs the core dependencies.
    ```bash
    uv sync
    ```

3.  **Configure API Keys:**
    * Create a `.env` file from the example: `cp .env.example .env`
    * Open `.env` and add your `GOOGLE_API_KEY`.

4.  **Activate and Run:**
    ```bash
    source .venv/bin/activate
    python -m src.main
    ```

---

### For Developers (with Observability)

These instructions include installing `langfuse` for tracing and debugging the agents.

1.  **Clone the Repository and `cd` into it.**

2.  **Create and Sync the Full Development Environment:**
    * The `--all-extras` flag tells `uv` to install the optional `[dev]` dependencies listed in `pyproject.toml`.
    ```bash
    uv sync --all-extras
    ```

3.  **Configure API Keys:**
    * Create a `.env` file: `cp .env.example .env`
    * Open `.env` and add your **`GOOGLE_API_KEY`**, **`LANGFUSE_PUBLIC_KEY`**, and **`LANGFUSE_SECRET_KEY`**.

4.  **Activate and Run:**
    ```bash
    source .venv/bin/activate
    uv run python -m src.main
    # You will see a message that Langfuse is enabled.
    ```

## ⚙️ How to Use

Finova runs as an interactive command-line application.

1.  **Start the Assistant:**
    From the root of the project directory, run the main script:
    ```bash
    uv run python -m src.main
    ```

2.  **Interact with Finova:**
    Once running, you can start a conversation. Here are some examples:

    * **Record an expense:**
        > `User: I bought groceries for 50 dollars`
    * **Record an income:**
        > `User: I received my salary of 2000`
    * **Ask for your balance:**
        > `User: What's my current balance?`
    * **Retrieve transactions:**
        > `User: How much did I spend on food last week?`
    * **Set a financial goal:**
        > `User: I want to save up for a new laptop`
    * **Ask for financial advice:**
        > `User: What is a good way to start investing?`

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion, please fork the repo and create a pull request. A great place to start would be to create a new `feature/NewCoolAgent` branch!

## 📜 License

This project is distributed under the MIT License.