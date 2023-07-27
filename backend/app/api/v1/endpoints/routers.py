from fastapi import APIRouter

from api.v1.endpoints import example
from api.v1.endpoints import message
from api.v1.endpoints import user

api_router = APIRouter()

api_router.include_router(example.router, tags=["example"])
api_router.include_router(message.router, tags=["messages"])
api_router.include_router(user.router, tags=["user"])