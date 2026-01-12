from redis.asyncio import Redis

from src import config

import logging

logger = logging.getLogger(__name__)

async def get_redis():
    redis_client = Redis(
        host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASSWORD, decode_responses=True
    )
    await redis_client.ping()
    
    print("✅ Connected to Redis")
    return redis_client