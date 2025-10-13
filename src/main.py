import asyncio
import os
from dotenv import load_dotenv
from openinference.instrumentation.google_adk import GoogleADKInstrumentor
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from .agents.agent import finova
from .utils import call_agent_async

load_dotenv()

if os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"):
    from langfuse import get_client
    # Set up Langfuse for observability
    langfuse = get_client()
    if langfuse.auth_check():
        print("Langfuse client authenticated")
        print("Langfuse observability is ENABLED.")
        GoogleADKInstrumentor().instrument()
    else:
        print("Langfuse client authentication failed")
else:
    langfuse = None
    print("Langfuse observability is DISABLED. Set LANGFUSE keys to enable.")


# Initialize session service
session_service = InMemorySessionService()

initial_state = {
    "user:name": "User",
    "user:balance": 0,
    "user:financial_goals": []
}

async def main_async():
    APP_NAME = "Finova"
    USER_ID = "user"

    # Create session
    new_session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state,
    )
    SESSION_ID = new_session.id 

    runner = Runner(
        app_name = APP_NAME,
        agent = finova,
        session_service=session_service,
    )

    while True:
        user_input = input("User: ")

        if user_input.lower() in ["exit", "quit", "q"]:
            print("Finova: See You Later!")
            break

        response = await call_agent_async(user_input, runner, USER_ID, SESSION_ID)
        print(f"Finova: {response}")


def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
