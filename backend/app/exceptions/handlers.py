from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from exceptions.custom_excaptions import UserAlreadyExists


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
