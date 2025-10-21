from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from src.prompts import ADVISOR

from src.agents.sub_agents.search_agent import search_agent

financial_advisor = Agent(
    name="financial_advisor",
    model=ADVISOR.config.model,
    description="Specialized Agent for answering financial related topic",
    instruction=ADVISOR.prompt,
    tools=[AgentTool(search_agent)]
)