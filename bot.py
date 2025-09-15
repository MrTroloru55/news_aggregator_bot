# bot.py
# Логика aiogram: команды для пользователя

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN, OWNER_ID
from Data_base.db import add_channel, get_channels

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Привет! Я буду собирать новости и присылать тебе их по расписанию.\n"
                     "Добавь канал командой: /add https://t.me/example")

@dp.message_handler(commands=["add"])
async def add(msg: types.Message):
    if msg.from_user.id != OWNER_ID:
        return await msg.answer("У тебя нет прав.")
    parts = msg.text.split()
    if len(parts) < 2:
        return await msg.answer("Использование: /add ссылка")
    add_channel(parts[1])
    await msg.answer(f"Канал {parts[1]} добавлен.")

@dp.message_handler(commands=["list"])
async def list_channels(msg: types.Message):
    chans = get_channels()
    if chans:
        text = "Подписанные каналы:\n" + "\n".join(chans)
    else:
        text = "Каналов пока нет."
    await msg.answer(text)
