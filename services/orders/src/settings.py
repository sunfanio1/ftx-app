from pydantic import PostgresDsn
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    postgres_dsn: str
    host: str = "0.0.0.0"

    class Config:
        env_file = '.env'
        extra = "allow"