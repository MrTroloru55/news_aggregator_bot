# collector.py
# Сбор постов с каналов через Telethon

from telethon import TelegramClient
from config import API_ID, API_HASH
from Data_base.db import get_channels
import datetime

# создаём клиент Telethon (userbot)
client = TelegramClient("session", API_ID, API_HASH)

async def collect_posts(limit=15):
    """Собираем посты из подписанных каналов"""
    results = []
    channels = get_channels()
    for ch in channels:
        try:
            entity = await client.get_entity(ch)
            msgs = await client.get_messages(entity, limit=limit)
            for m in msgs:
                if m.text:
                    results.append({
                        "channel": ch,
                        "id": m.id,
                        "text": m.text,
                        "date": m.date
                    })
        except Exception as e:
            print(f"Ошибка с каналом {ch}: {e}")
    return results
