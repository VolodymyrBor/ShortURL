from typing import Optional
from functools import lru_cache
from contextlib import AbstractAsyncContextManager

import aioredis

from configs import config


class LinkCounter(AbstractAsyncContextManager):
    """Counter for links"""
    def __init__(self, conn: Optional[aioredis.Redis] = None):
        self.conn = conn

    async def connect(self):
        if self.conn and not self.conn.closed:
            return

        self.conn = await aioredis.create_redis_pool(address=config.REDIS.url)

    async def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()

    async def inc_link_counter(self, url_alias: str, amount: int = 1):
        if await self.conn.exists(url_alias) == 0:
            await self.conn.set(url_alias, amount)
        else:
            await self.conn.incrby(url_alias, amount)

    async def get_counter(self, url_alias: str) -> int:
        if await self.conn.exists(url_alias) == 0:
            return 0
        return int(await self.conn.get(url_alias))

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


@lru_cache()
def get_link_counter() -> LinkCounter:
    return LinkCounter()


link_counter = get_link_counter()
