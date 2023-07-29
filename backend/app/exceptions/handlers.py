from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException

from exceptions.custom_excaptions import UserAlreadyExists, AuthenticationError, \
    NotAuthenticatedError


async def user_already_exists_error_handler(_, exc: UserAlreadyExists) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "result": False,
                "error_type": "User already exists",
                "error_message": "USER ALREADY EXISTS",
            }
        ),
    )


async def authentication_error_handler(_, exc: AuthenticationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "result": False,
                "error_type": "AUTHENTICATION ERROR",
                "error_message": "USERNAME AND PASSWORD DO NOT MATCH "
                                 "OR USERNAME DOES NOT EXIST",
            }
        ),
    )


async def not_authenticated_error(_, exc: NotAuthenticatedError):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=jsonable_encoder(
            {
                "result": False,
                "error_type": " 401 UNAUTHORIZED",
                "error_message": "authentication failed"
            }
        ),
    )
