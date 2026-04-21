from datetime import datetime, UTC
from time import timezone

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {
        'message': "Hello World"
    }

@app.get('/posts/{framework}')
def read_post(framework: str):
    return {
        "posts": [
            {
                "title": f"Criando uma aplicação com {framework}",
                "date": datetime.now(UTC)
            },
            {
                "title": f"Internaciopnalizando uma app {framework}",
                "date": datetime.now(UTC)
            }
            ]
    }