import os
import logging
from datetime import datetime
from sqlalchemy.engine import Engine, create_engine
from typing_extensions import Optional
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker
from sqlalchemy.types import DECIMAL, TIMESTAMP, String, Integer

logger = logging.getLogger(__name__)

script_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = f"{script_dir}/finova.db"
DB_URL = f"sqlite:///{DB_PATH}"

logger.info(f"Database URL configured: {DB_URL}")
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP(), nullable=False)
    amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)
    type: Mapped[str] = mapped_column(String(8), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    subcategory: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

class Liability(Base):
    __tablename__ = "liabilities"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False, default="lump_sum")
    total_amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False) 
    amount_paid: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False, default=0) 
    monthly_payment: Mapped[Optional[DECIMAL]] = mapped_column(DECIMAL(10, 2), nullable=True) 
    payment_due_day: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    total_installments: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    installments_paid: Mapped[Optional[int]] = mapped_column(Integer, nullable=False, default=0)
    due_date: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP(), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

class FinancialGoal(Base):
    __tablename__ = "financial_goals"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False, default="saving") # e.g., saving, limit, income
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    target_amount: Mapped[Optional[DECIMAL]] = mapped_column(DECIMAL(10, 2), nullable=True)
    current_amount: Mapped[Optional[DECIMAL]] = mapped_column(DECIMAL(10, 2), nullable=True, default=None) 
    target_date: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP(), nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="in_progress") # e.g., in_progress, achieved

def initialize_db(engine: Engine) -> None:
    """Crete all the database tables"""
    Base.metadata.create_all(engine)
