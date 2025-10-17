from google.adk.agents import Agent

from src.prompts import WRITE_AGENT
from src.tools import get_current_time, insert_transaction_tool
from src.tools.user_tool import update_balance

write_agent = Agent(
    name="write_agent",
    model=WRITE_AGENT.config.model,
    description="An agent that specialized in writing transaction",
    instruction=WRITE_AGENT.prompt,
    tools=[get_current_time, insert_transaction_tool, update_balance]
)