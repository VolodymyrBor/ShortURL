from abc import ABC
from enum import Enum

from pydantic import BaseModel


class Environment(str, Enum):
    DEV = 'dev'
    PROD = 'prod'


class BaseAuthConfig(BaseModel, ABC):
    _scheme: str = NotImplemented

    HOST: str = 'localhost'
    PORT: int
    USERNAME: str = 'root'
    PASSWORD: str = 'root'
    DATABASE: str = 'shorturl'

    @property
    def url(self) -> str:
        # mysql://USERNAME:PASSWORD@HOST:PORT/DATABASE
        return f'{self._scheme}://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}'


class DataBaseConfig(BaseAuthConfig):
    _scheme = 'mysql'

    PORT: int = 3306


class RedisConfig(BaseAuthConfig):
    _scheme = 'redis'

    PORT: int = 6379
    DATABASE: int = 0


class Config(BaseModel):
    HOST: str = 'localhost'
    PORT: int = 8000
    RELOAD: bool = True
    SECRET_KEY: str = 'secret key'

    ENV: Environment = Environment.DEV

    DB: DataBaseConfig = DataBaseConfig()
    REDIS: RedisConfig = RedisConfig()
