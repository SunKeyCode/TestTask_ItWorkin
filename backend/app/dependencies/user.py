from typing import Dict, Any, Optional

from fastapi import Depends
from fastapi_users.models import UP
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies.db_session import get_db_session
from models.user import User, UserProfile


class CustomSQLAlchemyUserDatabase(SQLAlchemyUserDatabase):

    async def create(self, create_dict: Dict[str, Any]) -> UP:
        user = self.user_table(**create_dict)
        profile = UserProfile(user_id=user.id)
        user.profile = profile
        self.session.add(user)
        await self.session.commit()
        return user

    async def get_by_username(self, username: str) -> Optional[UP]:
        statement = select(self.user_table).where(
            func.lower(self.user_table.username) == func.lower(username)
        )
        return await self._get_user(statement)


async def get_user_db(session: AsyncSession = Depends(get_db_session)):
    yield CustomSQLAlchemyUserDatabase(session, User)
