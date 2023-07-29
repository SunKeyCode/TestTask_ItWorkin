import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")

# JWT authentication
SECRET = os.environ.get("SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

API_VERSION = "v1"

# main.py directory
BASE_DIR = Path(__file__).resolve().parents[1]

MEDIA_ROOT = BASE_DIR.parents[1] / "media/"

DEBUG = True
