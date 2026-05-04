from contextlib import asynccontextmanager

from fastapi import FastAPI
from controllers import post,auth
from database import database, metadata, engine
from models.post import posts



@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)
app.include_router(post.router)

