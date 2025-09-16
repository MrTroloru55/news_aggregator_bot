# main.py
import asyncio
from aiogram import Bot, Dispatcher
from bot import router
from collector import client
from scheduler import setup_scheduler
from Data_base.db import init_db
from config import BOT_TOKEN, API_ID, API_HASH

async def start_telethon():
    """Telethon клиент для сбора постов"""
    async with client:
        print("Telethon подключён")
        await client.run_until_disconnected()

async def on_startup(bot):
    """Выполняется при запуске бота"""
    print("Бот запущен")
    init_db()  # создаём БД
    setup_scheduler(bot)  # передаём bot в setup_scheduler
    # Запускаем Telethon параллельно
    asyncio.create_task(start_telethon())

async def main():
    """Главная функция для запуска бота"""
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Register the router from bot.py
    dp.include_router(router)
    
    # Register the startup handler
    dp.startup.register(on_startup)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())