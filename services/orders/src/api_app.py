import os
from typing import cast

import uvicorn
from fastapi import FastAPI

import sentry_sdk
from prometheus_fastapi_instrumentator import Instrumentator

from src.routes.v1 import orders
from src.settings import Settings


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI()
    settings = Settings()
    app.extra = {"settings": settings}
    app.include_router(orders.router, prefix="/api")
    return app

app = create_app(Settings)

Instrumentator().instrument(app).expose(app)

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,  # Включение трейсинга (0.0–1.0)
    environment="development",
    release="1.0.0",
)




if __name__ == "__main__":
    uvicorn.run(app,
        host="0.0.0.0",
        port=8000)
