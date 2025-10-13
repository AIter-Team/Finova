import os
from datetime import datetime
from sqlalchemy.engine import Engine, create_engine
from typing_extensions import Optional
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker
from sqlalchemy.types import DECIMAL, TIMESTAMP, String

script_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = f"{script_dir}/finova.db"
DB_URL = f"sqlite:///{DB_PATH}"

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

def initialize_db(engine: Engine) -> None:
    """Crete all the database tables"""
    Base.metadata.create_all(engine)
