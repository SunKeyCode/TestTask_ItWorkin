from typing import Sequence, Optional, Dict, Any

from fastapi_users.models import UP
from sqlalchemy import select, func, Select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base_class import BaseDBRepo
from models.user import User, UserProfile


class UserBDSearchRepo(BaseDBRepo):

    async def search_user_by_username_field(self, fragment: str) -> Sequence[User]:
        users = await self.session.scalars(
            select(User).where(
                User.username.like(f"%{fragment}%")
            )
        )

        return users.all()

    async def search_user_by_email_field(self, fragment: str) -> Sequence[User]:
        users = await self.session.scalars(
            select(User).where(
                User.email.like(f"%{fragment}%@%")
            )
        )

        return users.all()

    async def search_user(self, fragment: str) -> Sequence[User]:
        users_by_username = await self.search_user_by_username_field(fragment)
        users_by_email = await self.search_user_by_email_field(fragment)

        return list(users_by_email) + list(users_by_username)


class UserBDRepo(BaseDBRepo):

    def __init__(self, session: AsyncSession):
        super().__init__(session=session)
        self.db_model = User

    async def _get_user(self, statement: Select) -> User:
        user = await self.session.scalar(statement)

        return user

    async def create(self, create_dict: Dict[str, Any]) -> User:
        user = self.db_model(**create_dict)
        profile = UserProfile(user_id=user.id)
        user.profile = profile
        self.session.add(user)
        await self.session.commit()
        return user

    async def get_user_by_username(self, username: str) -> User:
        statement = select(self.db_model).where(
            func.lower(self.db_model.username) == func.lower(username)
        )

        return await self._get_user(statement)

    async def update(self, update_data: Dict[str, Any]) -> User:
        pass
