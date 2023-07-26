from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from configs import app_configs

DB_URL = "postgresql+asyncpg://{user}:{password}@{host}/{db_name}".format(
    user=app_configs.DB_USER,
    password=app_configs.DB_PASSWORD,
    host=app_configs.DB_HOST,
    db_name=app_configs.DB_NAME,
)

async_engine = create_async_engine(DB_URL, echo=app_configs.DEBUG)

async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)
