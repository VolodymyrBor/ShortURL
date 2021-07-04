from functools import lru_cache

import databases
import sqlalchemy

from configs import config


@lru_cache()
def get_database() -> databases.Database:
    return databases.Database(config.DB.url)


@lru_cache()
def get_metadata() -> sqlalchemy.MetaData:
    return sqlalchemy.MetaData()


database = get_database()
metadata = get_metadata()


async def connect():
    if not database.is_connected:
        await database.connect()


async def disconnect():
    if database.is_connected:
        await database.disconnect()
