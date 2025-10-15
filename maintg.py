from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
import asyncio
import os
from app.handlers import router

find_path = find_dotenv()
load_dotenv(find_path)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')