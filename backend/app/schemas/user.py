from pydantic import BaseModel

from schemas.media import MediaModelOut


class UserReadSchema(BaseModel):
    id: int
    username: str
    is_active: bool


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


class ProfileSchema(BaseModel):
    id: int
    phone: str | None
    avatar: MediaModelOut | None


class FullUserModelSchemaOut(BaseModel):
    id: int
    username: str
    is_active: bool
    profile: ProfileSchema
