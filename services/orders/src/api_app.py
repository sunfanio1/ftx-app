import uvicorn
from fastapi import FastAPI

from src.routes.v1 import orders

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(orders.router, prefix="/api")
    return app

if __name__ == "__main__":
    uvicorn.run(create_app())
