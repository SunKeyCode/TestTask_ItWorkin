from fastapi import APIRouter

from api.v1.endpoints import example
# from api.v1.endpoints import auth

api_router = APIRouter()

api_router.include_router(example.router, tags=["example"])
# api_router.include_router(auth.router, tags=["auth"])
