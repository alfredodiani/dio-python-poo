from fastapi import status, Response, APIRouter
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")


#Classe para receber como parametro no POST


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_posts(post: PostIn):
    # fake_db.append(post.model_dump())
    return post

@router.get('/', response_model = list[PostOut])
def read_posts(
    response: Response, 
    published: bool, 
    limit: int, 
    skip: int = 0
):
    
    return []


