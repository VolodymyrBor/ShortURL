from enum import Enum

from pydantic import BaseModel


class Environment(str, Enum):
    DEV = 'dev'
    PROD = 'prod'


class DataBaseConfig(BaseModel):
    HOST: str = 'localhost'
    PORT: int = 3306
    USERNAME: str = 'root'
    PASSWORD: str = 'root'
    DATABASE: str = 'shorturl'

    @property
    def url(self) -> str:
        # mysql://USERNAME:PASSWORD@HOST:PORT/DATABASE
        return f'mysql://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}'


class Config(BaseModel):
    HOST: str = 'localhost'
    PORT: int = 8000
    RELOAD: bool = True
    SECRET_KEY: str = 'secret key'

    DB: DataBaseConfig = DataBaseConfig()
    ENV: Environment = Environment.DEV
