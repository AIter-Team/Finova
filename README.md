# Finova: Agentic Financial Life Management

![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Google%20ADK-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Finova is an intelligent, agentic system designed to help you manage your entire financial life—not just as an assistant, but as a proactive partner in your financial decisions.

## ⚠️ Development Status

**This project is currently in a public testing phase.**

We are using a prototyping/lean methodology, which means we are developing this as a Minimum Viable Product (MVP) and will be improving it based on user feedback. We encourage you to test the system and send us your thoughts for further improvement.

Please be aware that Finova is an experimental application. Features may change, and the current version is not recommended for managing real financial data. It is intended for demonstration and development purposes only.

## What is Finova?

Finova's goal is to manage your complete financial life, moving beyond simple transaction logging or budgeting. It's designed to help you make informed financial decisions, as many actions in life correspond with money.

Traditional finance apps often act as simple ledgers, requiring manual input and providing limited insight. Finova is built on a powerful **agentic architecture**. It operates not as a single program, but as a team of specialist agents that collaborate to understand your needs, manage complex tasks, and help you fully manage your financial decisions by integrating features like wishlist, financial goals, and liabilities management, and also investment advisory (soon).

## Core Features

* **Natural Language Interaction:** Simply talk to Finova as your friend.
* **Transaction Management:** Easily record income and expenses, and retrieve transaction history.
* **Budget Management:** Set and manage monthly income and expense budgets.
* **Financial Goal Setting:** Define and track saving, spending limit, or income goals.
* **Liability Tracking:** Record and manage lump-sum or installment liabilities (debts).
* **Wishlist Management:** Keep track of items you want or need to buy, including estimated prices and priority.
* **Financial Advice:** Get answers to finance-related questions using integrated search capabilities.
* **Stateful Memory:** Finova remembers your profile (name, language, currency) and balance across conversations for a personalized experience.

* **Optional Observability (For Developer):** Integrated with Langfuse to provide clear observability into agent performance and behavior for developers.

## Getting Started

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
    git clone https://github.com/AIter-Team/Finova
    cd finova
    ```

2.  **Create and Sync the Environment:**
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

## How to Use?

Finova runs as an interactive command-line application.

1.  **Start the Application:**
    From the root of the project directory, run the main script:
    ```bash
    uv run python -m src.main
    ```

2.  **Interact with Finova:**
    Once running, you can start a conversation. Here are some examples:

    * **Initial Setup (if new user):** Finova will ask for your name, language, and currency preference.
    * **Record an expense:**
        > `User: I bought groceries for 50 dollars`
    * **Record an income:**
        > `User: I received my salary of 2000`
    * **Ask for your balance:**
        > `User: What's my current balance?`
    * **Retrieve transactions:**
        > `User: How much did I spend on food last week?`
    * **Set a monthly budget:**
        > `User: I want to set my monthly budget`
    * **Set a financial goal:**
        > `User: I want to save up for a new laptop`
    * **Add a liability:**
        > `User: I need to record my car loan`
    * **Add to wishlist:**
        > `User: I want to buy a new gaming console`
    * **Ask for financial advice:**
        > `User: What is a good way to start investing?`

## 🤝 Contributing
Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## 📜 License
This project is distributed under the MIT License.
