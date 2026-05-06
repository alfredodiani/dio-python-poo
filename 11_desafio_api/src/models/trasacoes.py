from sqlalchemy import TIMESTAMP, Column, Enum as SAEnum, ForeignKey, Integer, Numeric, Table, text
from enum import Enum
from ..database import metadata

class TipoTransacao(str, Enum):
    DEPOSITO = "DEPOSITO"
    SAQUE = "SAQUE"


trasacoes = Table(
    "trasacoes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("conta_id", Integer, ForeignKey("conta_corrente.id"), nullable=False),
    Column("valor", Numeric(12, 2), nullable=False),
    Column("tipo", SAEnum(TipoTransacao, name="tipo_transacao"), nullable=False),
    Column("criado_em", TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

)