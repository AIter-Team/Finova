from google.adk.tools.tool_context import ToolContext

def update_user_profile(name: str, language: str, currency: str, tool_context: ToolContext) -> dict:
    """
    Udate current user name
    Use only when user name is not provided.

    Args:
        name (str): User name

    Returns:
        dict: A dictionary confirming the action was successful and report updated balance
    """

    tool_context.state["user:name"] = name
    tool_context.state["user:language"] = language
    tool_context.state["user:currency"] = currency

    return {
        "status": "success",
        "message": "User Profile Successfully Created"
        }


def add_financial_goals(goals: str, tool_context: ToolContext) -> dict:
    """
    Add new user financial goals

    Args:
        goals (str): String of user defined financial goals

    Returns:
        dict: A dictionary confirming the action was successful
    """
    user_goals = tool_context.state.get("user:financial_goals", [])
    user_goals.append(goals)
    tool_context.state["user:financial_goals"] = user_goals
        
    return {
        "status": "success",
        "message": f"New user financial goals added: {goals}"
        }

def update_balance(transaction_amount: int, tool_context: ToolContext) -> dict:
    """
    Udate current user balance based on incoming transaction

    Args:
        transaction_amount (int): Amount of recent user transaction.
        Positive (plus) if an income, negative (minus) if an expense

    Returns:
        dict: A dictionary confirming the action was successful and report updated balance
    """

    balance = tool_context.state.get("user:balance", 0)
    balance += transaction_amount
    tool_context.state["user:balance"] = balance

    return {
        "status": "success",
        "message": f"Current user balance: {balance}"
        }


def check_balance(tool_context: ToolContext) -> dict:
    """
    Check current user balance

    Returns:
        dics: A dictionary contains status and report of current user balance
    """

    balance = tool_context.state.get("user:balance", 0)
    if balance >= 0:
        return {
            "status": "success",
            "report": f"Current user balance: {balance}"
        }
    else:
        return {
            "status": "ValueError",
            "report": "There is an error in user balance value"
        }

def insert_liabilites(new_liability: dict, tool_context: ToolContext) -> dict:
    """
    Insert some liabilities

    """

    liabilities = tool_context.state.get("user:liabilites", [])
    pass

