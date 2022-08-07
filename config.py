import os
from functools import lru_cache
from pydantic import BaseSettings


####### Settings #######


class Settings(BaseSettings):
    secret: str = os.getenv("SECRET")
    algorithm: str = os.getenv("ALGORITHM")
    default_expiration_time: int = os.getenv("DEFAULT_EXPIRATION_TIME")

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
