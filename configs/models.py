from enum import Enum

from pydantic import BaseModel


class Environment(str, Enum):
    DEV = 'dev'
    PROD = 'prod'


class Config(BaseModel):
    HOST: str = 'localhost'
    PORT: int = 8000
    RELOAD: bool = True

    ENV: Environment = Environment.DEV
