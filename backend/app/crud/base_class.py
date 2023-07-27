from sqlalchemy.ext.asyncio import AsyncSession


class BaseDBManager:
    def __init__(self, session: AsyncSession):
        self.session = session
