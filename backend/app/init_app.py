from fastapi import FastAPI

from api.v1.endpoints.api_routers import api_router
from api.v1.endpoints.auth import auth_router
from exceptions import handlers
from configs import app_configs
from exceptions.custom_excaptions import UserAlreadyExists


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router, prefix=f"/api/{app_configs.API_VERSION}")
    app.include_router(auth_router)

    app.add_exception_handler(
        exc_class_or_status_code=UserAlreadyExists,
        handler=handlers.user_already_exists_error_handler
    )

    return app
