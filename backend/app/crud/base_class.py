from sqlalchemy.ext.asyncio import AsyncSession


class BaseDBRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
