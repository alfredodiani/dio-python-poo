from sqlalchemy import TIMESTAMP, Column, Integer, Numeric, Table, func

from src.database import metadata

accounts = Table(
    "accounts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False, index=True),
    Column("balance", Numeric(10, 2), nullable=False, default=0),
    Column("created_at", TIMESTAMP(timezone=True), default=func.now())
)