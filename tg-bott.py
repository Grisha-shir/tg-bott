import asyncio
from aiogram import Bot, Dispatcher
from antiflood import AntiFloodMiddleware
from config import TOKEN
from handlers.commands import command_router
from handlers.callback import callback_router
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

dp.message.middleware(AntiFloodMiddleware())

dp.include_router(command_router)
dp.include_router(callback_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
