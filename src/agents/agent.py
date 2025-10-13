from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from src.prompts import FINOVA
from src.tools import add_financial_goals, update_balance, check_balance

from .sub_agents.financial_advisor import financial_advisor
from .sub_agents.read_agent import read_agent
from .sub_agents.write_agent import write_agent

finova = Agent(
    name="finova",
    model=FINOVA.config.model,
    description="Main Personal financial assistant agent",
    instruction=FINOVA.prompt,
    sub_agents=[write_agent, read_agent],
    tools=[
        AgentTool(financial_advisor),
        add_financial_goals,
        update_balance,
        check_balance,
        ],
)