from db_alchemy.session import async_session


async def get_db_session():
    async with async_session() as session:
        yield session
