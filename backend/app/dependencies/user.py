from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies.db_session import get_db_session
from models.user import User


async def get_user_from_db(session: AsyncSession = Depends(get_db_session)):
    pass

