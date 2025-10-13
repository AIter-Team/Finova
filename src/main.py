import asyncio
import os
from dotenv import load_dotenv
from openinference.instrumentation.google_adk import GoogleADKInstrumentor
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from sqlalchemy import create_engine

from .db import DB_PATH, engine, initialize_db
from .agents.agent import finova
from .utils import call_agent_async

load_dotenv()

# Session Setup
session_service = InMemorySessionService()

# Initial State Setup
initial_state = {
    "user:name": "User",
    "user:balance": 0,
    "user:financial_goals": []
}

# Langfuse Setup
def setup_tracing():
    """Setup tracing for observability"""
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

# Database Setup
def setup_database():
    """Check for the database and initialize if it not found"""
    if not os.path.exists(DB_PATH):
        print("Database not found. Initializing...")
        try:
            initialize_db(engine)
            print(f"Database created successfully at: {DB_PATH}")
        except Exception as e:
            print(f"Error initializing database: {e}")
            raise
    else:
        print("Database already exists")

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
    setup_tracing()
    setup_database()
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
