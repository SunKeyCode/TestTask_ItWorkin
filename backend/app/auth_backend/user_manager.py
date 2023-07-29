from typing import Optional

from fastapi import Depends

from auth_backend.utils.password_helper import PasswordHelper
from crud.user import UserBDRepo
from dependencies.db_session import get_db_session
from exceptions.custom_excaptions import UserAlreadyExists, AuthenticationError
from models.user import User
from schemas.user import UserCreateSchema, UserAuthSchema, UserUpdateSchema


class UserManager:

    def __init__(
            self, db_manager: UserBDRepo,
            password_helper: Optional[PasswordHelper] = None,
    ):
        self.db_manager = db_manager
        if password_helper is None:
            self.password_helper = PasswordHelper()
        else:
            self.password_helper = password_helper

    async def create(self, user_data: UserCreateSchema):
        user_dict = user_data.model_dump()

        user_exists = await self.db_manager.get_user_by_username(user_data.username)
        if user_exists:
            raise UserAlreadyExists

        password = user_dict.pop("password")

        hashed_password = self.password_helper.hash(password)

        user_dict["hashed_password"] = hashed_password
        user = await self.db_manager.create(user_dict)

        return user

    async def get_user(self, username: str):
        return await self.db_manager.get_user_by_username(username)

    async def get_profile(self, user_id: int):
        return await self.db_manager.get_profile(user_id)

    async def update(self, user_data: UserUpdateSchema, user_to_update: User):
        data_to_update = user_data.model_dump()
        username = data_to_update.get("username")
        if username is not None:
            user_exists = await self.db_manager.get_user_by_username(username)
            if user_exists is not None:
                raise UserAlreadyExists

        user = await self.db_manager.update(
            data_to_update,
            user_to_update,
        )

        return user

    async def authenticate(self, credentials: UserAuthSchema) -> User:
        user: User = await self.db_manager.get_user_by_username(credentials.username)
        if user is None:
            raise AuthenticationError

        verified = self.password_helper.verify(
            credentials.password,
            user.hashed_password,
        )
        if verified:
            return user

        raise AuthenticationError


async def get_user_manager(session=Depends(get_db_session)):
    yield UserManager(UserBDRepo(session=session))
