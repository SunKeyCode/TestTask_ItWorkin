from typing import Sequence, Optional, Dict, Any

from sqlalchemy import select, func, Select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

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
        async with self.session.begin():
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

    async def get_profile(self, user_id: int):
        statement = select(self.db_model).where(self.db_model.id == user_id).options(
            joinedload(User.profile)
        )

        return await self._get_user(statement)

    async def update_profile(self, update_data: Dict[str, Any], user: User):
        async with self.session.begin():
            user_with_profile: User = await self.session.scalar(
                select(User).where(User.id == user.id).options(
                    joinedload(User.profile)
                )
            )
            for key in update_data:
                user_with_profile.profile.__setattr__(key, update_data[key])

        return user_with_profile

    async def update(self, update_data: Dict[str, Any], user: User) -> User:
        async with self.session.begin():
            if update_data.get("username"):
                user.username = update_data.pop("username")

        if update_data:
            user = await self.update_profile(update_data, user)

        return user
