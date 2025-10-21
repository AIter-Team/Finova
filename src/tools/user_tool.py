import logging
from typing_extensions import Optional
from datetime import datetime
from decimal import Decimal

from sqlalchemy.exc import SQLAlchemyError
from google.adk.tools.tool_context import ToolContext

from src.db import Liability, Session, FinancialGoal, Wishlist

logger = logging.getLogger(__name__)

# User preference
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
    tool_context.state["user:profiled"] = True

    return {
        "status": "success",
        "message": "User Profile Successfully Created"
        }

logger = logging.getLogger(__name__)

def add_financial_goal(
    description: str,
    type: str,
    target_amount: Optional[float] = None,
    target_date: Optional[str] = None
) -> dict:
    """
    Adds a new financial goal to the database.

    Args:
        description (str): A description of the goal (e.g., "Save for vacation", "Limit food spending").
        type (str): The type of goal ('saving', 'limit', 'income', 'other').
        target_amount (float, optional): The target amount for the goal.
        target_date (str, optional): The target date to achieve the goal (format YYYY-MM-DD).

    Returns:
        dict: A dictionary confirming the action status.
    """
    session = Session()
    try:
        parsed_target_date = None
        if target_date:
            try:
                parsed_target_date = datetime.strptime(target_date, "%Y-%m-%d")
            except ValueError:
                return {"status": "error", "message": "Invalid target_date format. Please use YYYY-MM-DD."}
        
        # Set current_amount to 0 if it's a 'saving' goal, else None
        initial_current_amount = None
        if type == 'saving':
            initial_current_amount = Decimal('0.0')

        new_goal = FinancialGoal(
            description=description,
            type=type.lower(),
            target_amount=Decimal(str(target_amount)) if target_amount else None,
            current_amount=initial_current_amount,
            target_date=parsed_target_date,
            status="in_progress"
        )
        
        session.add(new_goal)
        session.commit()
        
        logger.info(f"New financial goal added: {description}")
        return {
            "status": "success",
            "message": f"New financial goal '{description}' has been added."
        }

    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Error adding financial goal: {e}")
        return {"status": "error", "message": f"Database error: {e}"}
    finally:
        session.close()

def get_financial_goals() -> dict:
    """
    Retrieves all financial goals from the database.

    Returns:
        dict: A dictionary containing the status and a list of goals.
    """
    session = Session()
    try:
        goals = session.query(FinancialGoal).all()
        
        goals_list = []
        for goal in goals:
            goals_list.append({
                "id": goal.id,
                "description": goal.description,
                "type": goal.type,
                "target_amount": float(goal.target_amount) if goal.target_amount else None,
                "current_amount": float(goal.current_amount) if goal.current_amount else None,
                "target_date": goal.target_date.strftime("%Y-%m-%d") if goal.target_date else None,
                "status": goal.status
            })
            
        return {"status": "success", "goals": goals_list}

    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Error getting financial goals: {e}")
        return {"status": "error", "message": f"Database error: {e}"}
    finally:
        session.close()

def update_financial_goal(
    goal_id: int, 
    current_amount: Optional[float] = None, 
    status: Optional[str] = None
) -> dict:
    """
    Updates a financial goal's progress (current_amount) or its status.

    Args:
        goal_id (int): The ID of the goal to update.
        current_amount (float, optional): The new current amount (e.g., to track saving progress).
        status (str, optional): The new status (e.g., 'in_progress', 'achieved', 'cancelled').

    Returns:
        dict: A dictionary confirming the action status.
    """
    session = Session()
    try:
        goal = session.query(FinancialGoal).filter(FinancialGoal.id == goal_id).first()
        
        if not goal:
            return {"status": "error", "message": f"Goal with ID {goal_id} not found."}

        if current_amount is not None:
            goal.current_amount = Decimal(str(current_amount))
            logger.info(f"Updated goal {goal_id} current_amount to {current_amount}")

        if status is not None:
            goal.status = status
            logger.info(f"Updated goal {goal_id} status to {status}")

        session.commit()
        
        return {
            "status": "success", 
            "message": f"Goal {goal_id} ('{goal.description}') has been updated."
        }

    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Error updating financial goal: {e}")
        return {"status": "error", "message": f"Database error: {e}"}
    finally:
        session.close()


# User financial
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
        dict: A dictionary contains status and report of current user balance
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


def check_networth(tool_context: ToolContext) -> dict:
    """
    Check user networth (by subtracting balance with liabilites)

    Returns:
        dict: A dictionary that contain status and report of the current user networth
    """

    balance = tool_context.state.get("user:balance", 0)
    
    session = Session()

    pass

def set_income_budget(tool_context: ToolContext, **kwargs) -> dict:
    """
    Set or update the user's monthly INCOME budget categories.
    For example: salary, bonus, freelance_project, etc.

    Args:
        tool_context (ToolContext): The context object for accessing state.
        **kwargs: Income budget categories and their amounts (e.g., salary=5000, bonus=1000).

    Returns:
        dict: A dictionary confirming the action and listing the current income budget.
    """
    # Ambil budget pemasukan yang sudah ada, atau buat baru jika belum ada
    income_budget = tool_context.state["user:budget"].get("income", {})
    
    # Update dengan nilai baru dari kwargs
    income_budget.update(kwargs)
    
    # Simpan kembali ke state
    tool_context.state["user:budget"]["income"] = income_budget
    
    return {
        "status": "success",
        "message": "Income budget has been updated.",
        "current_income_budget": income_budget
    }


def set_expense_budget(tool_context: ToolContext, **kwargs) -> dict:
    """
    Set or update the user's monthly EXPENSE budget categories.
    For example: Food, Transport, Entertainment, etc.

    Args:
        tool_context (ToolContext): The context object for accessing state.
        **kwargs: Expense budget categories and their amounts (e.g., Food=500, Transport=200).

    Returns:
        dict: A dictionary confirming the action and listing the current expense budget.
    """
    # Ambil budget pengeluaran yang sudah ada, atau buat baru jika belum ada
    expense_budget = tool_context.state["user:budget"].get("expense", {})
    
    # Update dengan nilai baru dari kwargs
    expense_budget.update(kwargs)
    
    # Simpan kembali ke state
    tool_context.state["user:budget"]["expense"] = expense_budget
    
    return {
        "status": "success",
        "message": "Expense budget has been updated.",
        "current_expense_budget": expense_budget
    }


def add_liability(
    name: str,
    category: str,
    total_amount: float,
    amount_paid: float = 0.0,
    monthly_payment: Optional[float] = None,
    payment_due_day: Optional[int] = None,
    total_installments: Optional[int] = None,
    installments_paid: Optional[int] = 0,
    due_date: Optional[str] = None,
    notes: Optional[str] = None
) -> dict:
    """
    Adds a new liability (debt) to the database.

    Args:
        name (str): Name of the liability (e.g., "Car Loan", "Debt to John").
        category (str): Type of liability ('lump_sum' or 'installment').
        total_amount (float): The total principal amount of the debt.
        amount_paid (float, optional): The amount already paid off. Defaults to 0.0.
        monthly_payment (float, optional): The monthly payment amount (for 'installment').
        payment_due_day (int, optional): The day of the month payment is due (1-31) (for 'installment').
        total_installments (int, optional): Total number of installments (e.g., 3, 6, 12).
        installments_paid (int, optional): Number of installments already paid. Defaults to 0.
        due_date (str, optional): The final due date (for 'lump_sum'), format YYYY-MM-DD.
        notes (str, optional): Additional notes.

    Returns:
        dict: A dictionary confirming the action status.
    """
    session = Session()
    try:
        parsed_due_date = None
        if due_date:
            try:
                parsed_due_date = datetime.strptime(due_date, "%Y-%MM-%DD")
            except ValueError:
                return {"status": "error", "message": "Invalid due_date format. Please use YYYY-MM-DD."}
        
        new_liability = Liability(
            name=name,
            category=category,
            total_amount=Decimal(str(total_amount)),
            amount_paid=Decimal(str(amount_paid)),
            monthly_payment=Decimal(str(monthly_payment)) if monthly_payment else None,
            payment_due_day=payment_due_day,
            total_installments=total_installments,
            installments_paid=installments_paid,
            due_date=parsed_due_date,
            notes=notes
        )
        
        session.add(new_liability)
        session.commit()
        
        logger.info(f"New liability added: {name}")
        return {
            "status": "success",
            "message": f"New liability '{name}' for {total_amount} has been added."
        }

    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Error adding liability: {e}")
        return {"status": "error", "message": f"Database error: {e}"}
    except Exception as e:
        session.rollback()
        logger.error(f"Unexpected error: {e}")
        return {"status": "error", "message": f"Unexpected error: {e}"}
    finally:
        session.close()

# Wishlist

def add_wishlist(
    item_name: str,
    type: str,
    priority: str,
    estimated_price: Optional[float],
    notes: Optional[str]
):
    """
    Add new user wishlist to the database

    Args:
        item_name (str): Wishlist item name
        type (str): User wishlist type ["needs", "wants"]
        priority (str): Wishlist priority ["low", "medium", "high"]
        estimated_price (float, optional): Estimated price of the item
        notes (str, optional): Additional notes

    Returns:
        A dict that contain status and the message of the tool result
    """

    session = Session()

    try:
        new_item = Wishlist(
            item_name=item_name,
            type=type.lower(),
            priority=priority.lower(),
            estimated_price=Decimal(str(estimated_price)) if estimated_price else None,
            notes=notes,
            status="pending"
        )

        session.add(new_item)
        session.commit()

        logger.info(f"New wishlist added: {item_name}")
        return {
            "status": "success",
            "message": f"Successfully add new wishlist: {item_name}"
        }

    except Exception as e:
        session.rollback()
        logger.error(f"Error adding wishlist: {e}")
        return {
            "status": "error",
            "message": f"Error while adding new wishlist {e}"
        }
    finally:
        session.close()
