from google.adk.agents import Agent

from src.prompts import LIABILITY_AGENT
from src.tools import add_liability

liability_agent = Agent(
    name="liability_agent",
    model=LIABILITY_AGENT.config.model,
    description="Agent that specialized in managing liabilities",
    instruction=LIABILITY_AGENT.prompt,
    tools=[add_liability]
)