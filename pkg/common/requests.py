import asyncio
import aiohttp
import orjson # Utilize orjson for faster JSON serialization/deserialization
from typing import TypeVar

T = TypeVar('T')

class Requests:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def get(self, url: str, dataType: T, **kwargs) -> T:
        async with self.session.get(url, **kwargs) as response:
            return await response.json(loads=orjson.loads)

    async def post(self, url: str, dataType: T, **kwargs) -> T:
        async with self.session.post(url, **kwargs) as response:
            return await response.json(loads=orjson.loads)

    async def close(self):
        await self.session.close()