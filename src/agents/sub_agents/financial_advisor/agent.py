from google.adk.agents import Agent
from src.prompts import ADVISOR

financial_advisor = Agent(
    name="financial_advisor",
    model=ADVISOR.config.model,
    description="Specialized Agent for answering financial related topic",
    instruction=ADVISOR.prompt,
)