from datetime import datetime
from decimal import Decimal
from typing_extensions import Optional

from sqlalchemy.orm import Session

from src.db import engine, Transaction

def insert_transaction_tool(
    timestamp: str,
    amount: int,
    type: str,
    description: str,
    category: str,
    subcategory: Optional[str],
    notes: Optional[str],
) -> dict:
    """Insert a transaction into the database
    
    Args: 
        timestamp (str): Transaction date
        amount (str): Amount of the transaction
        type (str): Transaction type (income or expense) 
        description (str): The transaction description 
        category (str): Transaction category
        subcategory (str): Optional sub-category based on the transaction category
        notes (str): Optional notes specified by the user
    
    Returns:
        dict: A dictionary containing the transaction record.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'summary' key with weather details.
              If 'error', includes an 'error_message' key.
    """

    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    amount = Decimal(amount)
    session = Session(bind=engine)

    new_transaction = Transaction(
        timestamp=timestamp,
        amount=amount,
        type=type.lower(),
        description=description,
        category=category.lower(),
        subcategory=subcategory.lower(),
        notes=notes,
    )
    session.add(new_transaction)
    session.commit()
    session.close()

    return {
        "status": "success",
        "summary": (
            "Transaction recorded successfully..\n"
            f"Type: {type}\n"
            f"Amount: {amount}\n"
            f"Timestamp: {timestamp}\n"
            f"Description: {description}\n"
            f"Category: {category}\n"
            f"Sub Category: {subcategory}\n"
            f"Notes: {notes}"
            )
        }

def read_transaction_tool():
    pass