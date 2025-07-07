from typing import AsyncGenerator

from sqlalchemy.orm import Session

from services.orders.src.database.postgresql import PGConnector


async def get_session_pg(settings) -> AsyncGenerator[Session, None]:
    pg_connect = PGConnector(settings)
    db = pg_connect.pg_session()

    try:
        yield db
    finally:
        db.close()
