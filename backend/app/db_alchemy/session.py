from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from configs import app_configs


DB_URL = "{driver}:///{filename}".format(
    driver=app_configs.DB_DRIVER,
    filename=app_configs.DB_FILENAME,
)

async_engine = create_async_engine(DB_URL, echo=app_configs.DEBUG)

async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)
