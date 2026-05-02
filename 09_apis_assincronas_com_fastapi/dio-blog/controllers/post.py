from fastapi import status, APIRouter
from schemas.post import PostIn, PostUpdateIn
from views.post import PostOut
from models.post import posts
from database import database
from services.post import PostService

service = PostService()

router = APIRouter(prefix="/posts")


@router.get("/{id}", response_model = PostOut)
async def read_post(id: int):
    return await service.read(id)

@router.get("/", response_model = list[PostOut])
async def read_posts(published: bool, limit: int, skip: int = 0):
    return await service.read_all(published, limit, skip)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_posts(post: PostIn):
    return {**post.model_dump(), "id": await service.create(post)}
    
@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await service.update(id=id, post=post)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
    await service.delete(id)