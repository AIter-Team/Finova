from google.adk.agents import Agent


preference_agent = Agent(
    name="preference_agent",
    model="gemini-2.5-flash",
    description="Agent that help notes user preference"
)