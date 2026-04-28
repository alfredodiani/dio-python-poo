from pydantic import BaseModel
from datetime import datetime, UTC

class PostIn(BaseModel):
    tittle: str
    date: datetime = datetime.now(UTC)
    published: bool = False