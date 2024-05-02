from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from config import Settings


redis = aioredis.from_url(url=Settings.REDIS_DSN, encoding="utf8", decode_responses=True)
backend = RedisBackend(redis)