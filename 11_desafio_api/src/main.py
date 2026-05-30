from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from fastapi.responses import JSONResponse

from src.exceptions import AccountNotFoundError, BusinessError

from src.controllers import account, auth, transaction
from src.database import database, metadata, engine



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


app = FastAPI(
    title="Transactions API",
    version="1.1",
    summary="Microservice to maintain withdrawal and deposit operations from current accounts.",
    description="""
Transactions API is the microservice for recording current account transactions.

## Account

* **Create accounts**.
* **List accounts**.
* **List account transactions by ID**.

## Transaction

* **Create transactions**.
    """,
    openapi_tags=[
        {
            "name": "auth",
            "description": "Operations for authentication.",
        },
        {
            "name": "account",
            "description": "Operations to maintain accounts.",
        },
        {
            "name": "transaction",
            "description": "Operations to maintain transactions.",
        },
    ],
    redoc_url=None,
    lifespan=lifespan
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["auth"])
app.include_router(account.router, tags=["account"])
app.include_router(transaction.router, tags=["transaction"])


@app.exception_handler(AccountNotFoundError)
def account_not_found_error_handler(request: Request, exc: AccountNotFoundError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Account not found."})


@app.exception_handler(BusinessError)
def business_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)})