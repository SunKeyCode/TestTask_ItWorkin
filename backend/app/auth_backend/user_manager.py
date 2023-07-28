from fastapi import Depends

from crud.user import UserBDRepo
from dependencies.db_session import get_db_session
from exceptions.custom_excaptions import UserAlreadyExists
from schemas.user import UserCreateSchema


class UserManager:

    def __init__(self, db_manager: UserBDRepo):
        self.db_manager = db_manager

    async def create(self, user_data: UserCreateSchema):
        user_dict = user_data.model_dump()

        user_exists = self.db_manager.get_user_by_username(user_data.username)
        if user_exists:
            raise UserAlreadyExists

        password = user_dict.pop("password")
        user_dict["hashed_password"] = password
        user = await self.db_manager.create(user_dict)

        return user


async def get_user_manager(session=Depends(get_db_session)):
    yield UserManager(UserBDRepo(session=session))
