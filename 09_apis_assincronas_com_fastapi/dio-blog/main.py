from datetime import datetime, UTC

from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {
        "title": "Criando uma aplicação com FastAPI",
        "date": datetime.now(UTC),
        "published": True
    },
    {
        "title": "Criando uma aplicação com Django",
        "date": datetime.now(UTC),
        "published": False
    },
    {
        "title": "Criando uma aplicação com Flask",
        "date": datetime.now(UTC),
        "published": True
    },
    {
        "title": "Criando uma aplicação com Starlett",
        "date": datetime.now(UTC),
        "published": True
    }
]



@app.get('/posts')
def readposts(skip: int = 0, limit: int = len(fake_db), published: bool = True):
    return [post for post in fake_db[skip : skip + limit] if post['published'] is published]


@app.get('/')
def read_root():
    return {
        'message': "Hello World"
    }

@app.get('/posts/{framework}')
def read_framework_posts(framework: str):
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