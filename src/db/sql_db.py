import os
from datetime import datetime
from typing_extensions import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy.types import DECIMAL, TIMESTAMP, String

script_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = f"{script_dir}/finova.db"


url = f'sqlite:///{DB_PATH}'

engine = create_engine(url)

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


Base.metadata.create_all(engine)
