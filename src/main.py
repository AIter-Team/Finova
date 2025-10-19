import asyncio
import os
import logging
from dotenv import load_dotenv
from openinference.instrumentation.google_adk import GoogleADKInstrumentor
from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner

from .logging import setup_logging
from .db import DB_PATH, DB_URL, engine, initialize_db
from .agents.agent import finova
from .utils import call_agent_async

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

# Langfuse Setup
def setup_tracing():
    """Setup tracing for observability"""
    if os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"):
        from langfuse import get_client
        # Set up Langfuse for observability
        langfuse = get_client()
        if langfuse.auth_check():
            logger.info("Langfuse client authenticated")
            logger.info("Langfuse observability is ENABLED.")
            GoogleADKInstrumentor().instrument()
        else:
            logger.warning("Langfuse client authentication failed")
    else:
        langfuse = None
        logger.warning("Langfuse observability is DISABLED. Set LANGFUSE keys to enable.")

# Database Setup
def setup_database():
    """Check for the database and initialize if it not found"""
    if not os.path.exists(DB_PATH):
        logger.warning("Database not found. Initializing...")
        try:
            initialize_db(engine)
            logger.info(f"Database created successfully at: {DB_PATH}")
        except Exception as e:
            logger.critical(f"Error initializing database: {e}")
            raise
    else:
        logger.info("Database already exists. Skipping initialization.")

async def main_async(session_service, initial_state):
    APP_NAME = "Finova"
    USER_ID = "user"


    existing_sessions = await session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID
    )

    # Create session
    if existing_sessions and len(existing_sessions.sessions) > 0:
        new_session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
        )
    else:
        new_session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
    
    SESSION_ID = new_session.id 
    logger.info(f"Create new session: {SESSION_ID}")

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
    logger.info("==================== APPLICATION START ====================")

    setup_tracing()
    setup_database()

    # Session Setup
    session_service = DatabaseSessionService(db_url=DB_URL)

    # Initial State Setup
    initial_state = {
        "user:name": "User",
        "user:balance": 0,
        "user:language": "eng",
        "user:currency": "USD",
        "user:financial_goals": [],
        "user:budget": {
            "income": {},
            "expense": {}
        },
        "profiled": False
    }

    asyncio.run(main_async(session_service, initial_state))
    logger.info("==================== APPLICATION END ======================")

if __name__ == "__main__":
    main()
