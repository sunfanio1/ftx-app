from sqlalchemy import MetaData, create_engine

from sqlalchemy.orm import Session, declarative_base, sessionmaker


PGBase = declarative_base()
pg_metadata = MetaData()

class PGConnector:

    def __init__(self, settings) -> None:
        self.pg_engine = create_engine("postgresql://user:pass@host:port/dbname")
        self.pg_session = sessionmaker(self.pg_engine, class_=Session)
