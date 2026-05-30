from sqlalchemy import TIMESTAMP, Column, Enum as SAEnum, ForeignKey, Integer, Numeric, Table, func
from enum import Enum
from ..database import metadata

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


transactions = Table(
    "transactions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("account_id", Integer, ForeignKey("accounts.id"), nullable=False),
    Column("type", SAEnum(TransactionType, name="transaction_types"), nullable=False),
    Column("amount", Numeric(10, 2), nullable=False),
    Column("created_at", TIMESTAMP(timezone=True), default=func.now())

)