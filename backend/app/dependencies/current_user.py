from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies.db_session import get_db_session
from models.user import User
from auth_backend.auth_backend import get_user_by_jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db_session: AsyncSession = Depends(get_db_session),
) -> User:
    user = await get_user_by_jwt_token(db_session=db_session, token=token)
    return user
