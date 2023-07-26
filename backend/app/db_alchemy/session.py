from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configs import app_configs

DB_URL = "postgresql+psycopg2://{user}:{password}@{host}/{db_name}/".format(
    user=app_configs.DB_USER,
    password=app_configs.DB_PASSWORD,
    host=app_configs.DB_HOST,
    db_name=app_configs.DB_NAME,
)

engin = create_engine(DB_URL, echo=app_configs.DEBUG)

Session = sessionmaker(engin)
