from fastapi import FastAPI

from api.v1.endpoints.api_routers import api_router
from api.v1.endpoints.auth import auth_router
from configs import app_configs


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router, prefix=f"/api/{app_configs.API_VERSION}")
    app.include_router(auth_router)

    return app
