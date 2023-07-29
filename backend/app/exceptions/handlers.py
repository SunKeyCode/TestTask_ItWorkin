from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from starlette import status
from starlette.responses import JSONResponse

from exceptions.custom_excaptions import (
    UserAlreadyExists,
    AuthenticationError,
    NotAuthenticatedError,
)


async def user_already_exists_error_handler(_, exc: UserAlreadyExists) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                {
                    "detail": [
                        {
                            "type": "USER ALREADY EXISTS",
                            "msg": "user with this username already exists",
                        }
                    ]
                }
            }
        ),
    )


async def authentication_error_handler(_, exc: AuthenticationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                {
                    "detail": [
                        {
                            "type": "AUTHENTICATION ERROR",
                            "msg": "username and password do not match "
                            "or username does not exists",
                        }
                    ]
                }
            }
        ),
    )


async def not_authenticated_error(_, exc: NotAuthenticatedError):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=jsonable_encoder(
            {"detail": [{"type": "401 UNAUTHORIZED", "msg": "authentication failed"}]}
        ),
    )


async def integrity_error_handler(_, exc: IntegrityError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": "data base integrity error"}),
    )
