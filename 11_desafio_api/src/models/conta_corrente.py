from sqlalchemy import TIMESTAMP, Column, Integer, Numeric, String, Table, text

from ..database import metadata

conta_corrente = Table(
    "conta_corrente",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("titular", String(50), nullable=False),
    Column("saldo", Numeric(12, 2), nullable=False, server_default=text("0")),
    Column("criado_em", TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
)