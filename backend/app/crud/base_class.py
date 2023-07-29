from sqlalchemy.ext.asyncio import AsyncSession
from db_alchemy.session import async_session


class BaseDBRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
