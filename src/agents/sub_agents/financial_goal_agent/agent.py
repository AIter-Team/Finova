from google.adk.agents import Agent

from src.prompts import FINANCIAL_GOAL_AGENT
from src.tools.user_tool import add_financial_goal, update_financial_goal, get_financial_goals

financial_goal_agent = Agent(
    name="financial_goal_agent",
    model=FINANCIAL_GOAL_AGENT.config.model,
    description="Agent that specialized in managing user financial goals",
    instruction=FINANCIAL_GOAL_AGENT.prompt,
    tools=[add_financial_goal, update_financial_goal, get_financial_goals]
)