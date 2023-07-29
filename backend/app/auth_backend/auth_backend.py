from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from configs import app_configs
from crud.user import UserBDRepo
from exceptions.custom_excaptions import NotAuthenticatedError
from models.user import User


async def get_user_by_jwt_token(
        db_session: AsyncSession,
        token: str,
) -> User:
    if app_configs.SECRET is None:
        raise JWTError("SECRET_KEY is not set")

    try:
        payload = jwt.decode(
            token, app_configs.SECRET, algorithms=[app_configs.ALGORITHM]
        )
        username = payload.get("username")
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="TOKEN EXPIRED",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise NotAuthenticatedError

    if username is None:
        raise NotAuthenticatedError

    user: User | None = await UserBDRepo(session=db_session).get_user_by_username(
        username
    )

    if user is None:
        raise NotAuthenticatedError

    return user
