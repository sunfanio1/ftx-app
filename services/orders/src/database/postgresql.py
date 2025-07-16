from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import declarative_base, sessionmaker, Session

from src.settings import Settings

class PGConnector:

    def __init__(self, settings: Settings) -> None:
        print("settings", settings.postgres_dsn)
        self.pg_engine = create_engine(str(settings.postgres_dsn))
        self.pg_session = sessionmaker(self.pg_engine, class_=Session)


PGBase = declarative_base()
pg_metadata = MetaData()
