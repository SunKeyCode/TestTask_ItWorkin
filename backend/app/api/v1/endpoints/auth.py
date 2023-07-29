from fastapi import APIRouter, Depends

from auth_backend.user_manager import get_user_manager, UserManager
from dependencies.current_user import get_current_user
from models.user import User
from schemas.user import (
    UserCreateSchema,
    UserAuthSchema,
    UserUpdateSchema,
    UserCreateSchemaOut,
    FullUserModelSchemaOut,
)
from auth_backend.utils import jwt_token

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post(
    "/register",
    response_model=UserCreateSchemaOut,
)
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

    access_token = jwt_token.create_access_token({"username": user.username})

    return {"access_token": access_token, "token_type": "Bearer"}


@auth_router.patch(
    "/me/update",
    response_model=FullUserModelSchemaOut,
)
async def update_user(
    update_data: UserUpdateSchema,
    current_user: User = Depends(get_current_user),
    user_manger: UserManager = Depends(get_user_manager),
):
    updated_user = await user_manger.update(update_data, current_user)

    return updated_user


@auth_router.get(
    "/me",
    response_model=FullUserModelSchemaOut,
)
async def get_profile(
    current_user: User = Depends(get_current_user),
    user_manger: UserManager = Depends(get_user_manager),
):
    profile = await user_manger.get_profile(user_id=current_user.id)
    return profile
