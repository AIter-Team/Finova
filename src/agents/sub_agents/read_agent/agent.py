from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from src.tools import get_current_time
from src.prompts import READ_AGENT
from src.db import DB_PATH


read_agent = Agent(
    name="read_agent",
    model=READ_AGENT.config.model,
    description="Agent that specialized in reading transaction",
    instruction=READ_AGENT.prompt,
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args= [
                        "-y",
                        "@executeautomation/database-server",
                        f"{DB_PATH}"
                    ]
                )
            )
        )
    ]
)
