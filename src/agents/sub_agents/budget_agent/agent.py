from google.adk.agents import Agent

from src.prompts.budget_agent import BUDGET_AGENT
from src.tools import set_income_budget, set_expense_budget

budget_agent = Agent(
    name="budget_agent",
    model=BUDGET_AGENT.config.model,
    description="Agent that specialized in managing budget",
    instruction=BUDGET_AGENT.prompt,
    tools=[
        set_income_budget,
        set_expense_budget
    ]
)