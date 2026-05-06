from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database import database, metadata, engine
from .models import conta_corrente, trasacoes


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    metadata.create_all(engine)

    #printar no terminal todas as tabelas do banco de dados
    async with database.transaction():
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = await database.fetch_all(query)
        print("Tabelas no banco de dados:")
        for table in tables:
            print(table["name"])
    
    
    yield
    await database.disconnect()




app = FastAPI(lifespan=lifespan)

# Criar tabelas ao iniciar (opcional)
# metadata.create_all(engine)

