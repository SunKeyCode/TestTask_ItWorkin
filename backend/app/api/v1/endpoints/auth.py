from fastapi import APIRouter, Depends

from auth_backend.user_manager import get_user_manager, UserManager
from schemas.user import UserCreateSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/register")
async def register_user(
        user_data: UserCreateSchema,
        user_manger: UserManager = Depends(get_user_manager),
):
    user = await user_manger.create(user_data)
    return user_data


@auth_router.post("/login")
async def login():
    pass
