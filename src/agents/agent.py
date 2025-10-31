from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from src.prompts import FLO
from src.tools import check_balance, update_user_profile


from .sub_agents import financial_advisor, read_agent, write_agent, budget_agent, financial_goal_agent, liability_agent, wishlist_agent

flo = Agent(
    name="flo",
    model=FLO.config.model,
    description="Main Personal financial assistant agent",
    instruction=FLO.prompt,
    sub_agents=[
        write_agent,
        read_agent,
        budget_agent,
        financial_goal_agent,
        liability_agent,
        wishlist_agent,
        ],
    tools=[
        AgentTool(financial_advisor),
        check_balance,
        update_user_profile
        ],
)