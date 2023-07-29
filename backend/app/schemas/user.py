from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[int]):
    username: str


class UserCreateSchema(BaseModel):
    username: str
    password: str


class UserCreateSchemaOut(BaseModel):
    id: int
    username: str


class UserAuthSchema(BaseModel):
    username: str
    password: str


class UserUpdateSchema(BaseModel):
    username: str | None = None
    phone: str


class UserUpdateSchemaOut(BaseModel):
    pass


class ProfileSchema(BaseModel):
    id: int
    phone: str
