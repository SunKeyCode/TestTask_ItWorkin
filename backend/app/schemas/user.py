from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[int]):
    username: str


class UserCreateSchema(BaseModel):
    username: str
    password: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
