from typing import Sequence

from sqlalchemy import select

from crud.base_class import BaseDBManager
from models.user import User


class UserBDSearchManager(BaseDBManager):

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
