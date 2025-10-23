from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from src.prompts import WISHLIST_AGENT
from src.agents.sub_agents.search_agent import search_agent
from src.tools import add_wishlist, get_wishlists, get_current_time

wishlist_agent = Agent(
    name="wishlist_agent",
    model=WISHLIST_AGENT.config.model,
    description="Agent that responsible in managing user wishlist",
    instruction=WISHLIST_AGENT.prompt,
    tools=[
        AgentTool(search_agent), 
        add_wishlist,
        get_wishlists,
        get_current_time
    ]
)