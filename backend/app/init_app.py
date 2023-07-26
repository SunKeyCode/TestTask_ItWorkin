from fastapi import FastAPI

from api.v1.endpoints.routers import api_router
from api.v1.endpoints.auth import router
from configs import app_configs


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router, prefix=f"/api/{app_configs.API_VERSION}")
    app.include_router(router)

    return app
