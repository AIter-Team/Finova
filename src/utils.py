from google.genai import types

async def display_state(
    session_service, app_name, user_id, session_id, label="Current State"
):
    """Display the current session state in a formatted way."""
    try:
        session = await session_service.get_session(
            app_name=app_name, user_id=user_id, session_id=session_id
        )

        # Format the output with clear sections
        print(f"\n{'-' * 10} {label} {'-' * 10}")

        # Handle the user name
        user_name = session.state.get("user:name", "Unknown")
        print(f"User: {user_name}")

        balance = session.state.get("user:balance", 0)
        print(f"Balance: {balance}")

        language = session.state.get("user:language", 0)
        print(f"Language: {language}")

        currency = session.state.get("user:currency", 0)
        print(f"Currency: {currency}")

        # Handle reminders
        goals = session.state.get("user:financial_goals", [])
        if goals:
            print("Goals :")
            for idx, goal in enumerate(goals, 1):
                print(f"  {idx}. {goal}")
        else:
            print("Goals: None")

        print("-" * (22 + len(label)))
    except Exception as e:
        print(f"Error displaying state: {e}")

async def process_agent_response(event):
    
    print(f"Event ID: {event.id}, Author: {event.author}")

    final_response = None
    if event.is_final_response():
        if (
            event.content and event.content.parts
        ):
            final_response = event.content.parts[0].text

    return final_response

async def call_agent_async(query: str, runner, user_id, session_id):

    content = types.Content(role="user", parts=[types.Part(text=query)])

    final_response_text = None

    # Display state before processing
    await display_state(
        runner.session_service,
        runner.app_name,
        user_id,
        session_id,
        "State BEFORE processing",
    )

    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):

        response = await process_agent_response(event)
        if response:
            final_response_text = response

    # Display state after processing
    await display_state(
        runner.session_service,
        runner.app_name,
        user_id,
        session_id,
        "State AFTER processing",
    )

    return final_response_text