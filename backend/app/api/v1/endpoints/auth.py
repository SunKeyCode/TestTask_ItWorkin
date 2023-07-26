from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from auth_backend.auth_backend import bearer_jwt_auth_backend
from auth_backend.user_manager import get_user_manager
from models.users import User
from schemas.users import UserRead, UserCreate

router = APIRouter(prefix="/auth")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [bearer_jwt_auth_backend],
)

router.include_router(
    fastapi_users.get_auth_router(bearer_jwt_auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
