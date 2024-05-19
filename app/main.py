import asyncio
from aiogram import Bot, Dispatcher
from middleware import AntiThrottlingMiddleware
from config import settings
from database import database
from handlers import router

async def main():
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    dp.message.middleware(AntiThrottlingMiddleware(rate_limit=settings.rate_limit_message))
    
    dp.include_router(router)

    await database.connect()
    try:
        await dp.start_polling(bot)
    finally:
        await database.close()
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
