# main.py
import asyncio
from aiogram.utils import executor
from bot import dp
from collector import client
from scheduler import setup_scheduler
from Data_base.db import init_db
from config import API_ID, API_HASH, SESSION_NAME

async def start_telethon():
    # Telethon клиент для сбора постов
    async with client:
        print("Telethon подключён")
        await client.run_until_disconnected()

async def on_startup(dp):
    print("Бот запущен")
    init_db()           # создаём БД
    setup_scheduler()   # включаем планировщик
    # Запускаем Telethon параллельно
    asyncio.create_task(start_telethon())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
