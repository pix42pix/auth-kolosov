"""Redis client module."""

from aioredis import Redis, from_url


async def init_redis(host: str, password: str) -> Redis:
    return await from_url(f"redis://:{password}@{host}")
