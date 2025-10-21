from google.adk.agents import Agent
from google.adk.tools import google_search

search_agent = Agent(
    name="search_agent",
    model="gemini-2.5-flash",
    description="Agent that specialized in search using google search",
    instruction="You are search specialized agent",
    tools=[google_search]
)