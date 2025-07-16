from typing import AsyncGenerator

from fastapi import Depends, Request
from sqlalchemy.orm import Session

from src.database.postgresql import PGConnector
from src.repositories.orders.orders import OrdersRepository
from src.settings import Settings


async def get_settings(request: Request) -> Settings:
    settings: Settings = request.app.extra["settings"]
    return settings

async def get_session_pg(settings: Settings = Depends(get_settings)) -> AsyncGenerator[Session, None]:
    pg_connect = PGConnector(settings)
    db = pg_connect.pg_session()
    try:
        yield db
    finally:
        db.close()


async def get_orders_repository(session: Session = Depends(get_session_pg)) -> OrdersRepository:
    return OrdersRepository(session)