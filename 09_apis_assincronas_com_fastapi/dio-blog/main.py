from datetime import datetime, UTC
from fastapi import FastAPI, status
from pydantic import BaseModel


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

#Classe para receber como parametro no POST
class Post(BaseModel):
    tittle: str
    date: datetime = datetime.now(UTC)
    published: bool = False


    
@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    fake_db.append(post.model_dump())
    return post

@app.get('/posts')
def readposts(limit: int, skip: int = 0, published: bool = True):
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
