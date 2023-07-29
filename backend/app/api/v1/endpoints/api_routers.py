from fastapi import APIRouter

from api.v1.endpoints import message
from api.v1.endpoints import user
from api.v1.endpoints import media

api_router = APIRouter()

api_router.include_router(message.router, tags=["messages"])
api_router.include_router(user.router, tags=["user"])
api_router.include_router(media.router, tags=["media"])
