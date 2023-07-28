from fastapi import APIRouter, Depends

from auth_backend.user_manager import get_user_manager, UserManager
from schemas.user import UserCreateSchema, UserAuthSchema
from auth_backend.utils import jwt

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/register")
async def register_user(
        user_data: UserCreateSchema,
        user_manger: UserManager = Depends(get_user_manager),
):
    user = await user_manger.create(user_data)
    return user


@auth_router.post("/login")
async def login(
        credentials: UserAuthSchema,
        user_manger: UserManager = Depends(get_user_manager),
):
    user = await user_manger.authenticate(credentials)

    access_token = jwt.create_access_token({"username": user.username})

    return {"access_token": access_token, "token_type": "Bearer"}
