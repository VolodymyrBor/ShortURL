from abc import ABC
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Environment(str, Enum):
    DEV = 'dev'
    PROD = 'prod'


class BaseAuthConfig(BaseModel, ABC):
    _scheme: str = NotImplemented

    PORT: int
    HOST: str = 'localhost'
    DATABASE: str = 'shorturl'

    USERNAME: Optional[str] = None
    PASSWORD: Optional[str] = None

    @property
    def url(self) -> str:
        # mysql://USERNAME:PASSWORD@HOST:PORT/DATABASE
        return f'{self._scheme}://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}'


class DataBaseConfig(BaseAuthConfig):
    _scheme = 'mysql'

    USERNAME: str = 'root'
    PASSWORD: str = 'root'

    PORT: int = 3306


class RedisConfig(BaseAuthConfig):
    _scheme = 'redis'

    PORT: int = 6379
    DATABASE: int = 0
    PASSWORD: str = 'root'

    @property
    def url(self) -> str:
        if self.USERNAME:
            return super().url
        else:
            return f'{self._scheme}://{self.HOST}:{self.PORT}/{self.DATABASE}'


class Config(BaseModel):
    HOST: str = 'localhost'
    PORT: int = 8000
    RELOAD: bool = True
    SECRET_KEY: str = 'secret key'

    ENV: Environment = Environment.DEV

    DB: DataBaseConfig = DataBaseConfig()
    REDIS: RedisConfig = RedisConfig()
