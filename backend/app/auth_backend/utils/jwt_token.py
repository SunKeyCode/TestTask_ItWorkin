from datetime import datetime, timedelta

from jose import JWTError, jwt

from configs import app_configs


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(
        minutes=int(app_configs.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    if app_configs.SECRET is None:
        raise JWTError("SECRET_KEY is not set")

    return jwt.encode(
        claims=to_encode, key=app_configs.SECRET, algorithm=app_configs.ALGORITHM
    )
