import asyncio
from aiogram import BaseMiddleware
from aiogram.types import Message

class AntiThrottlingMiddleware(BaseMiddleware):
    def __init__(self, rate_limit=1):
        self.rate_limit = rate_limit
        self.users = {}

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        current_time = asyncio.get_event_loop().time()

        if user_id in self.users:
            last_time = self.users[user_id]
            if current_time - last_time < self.rate_limit:
                return 
        self.users[user_id] = current_time
        return await handler(event, data)
