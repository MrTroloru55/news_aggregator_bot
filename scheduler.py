# scheduler.py
# Планировщик (apscheduler) для сбора и отправки новостей

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from collector import collect_posts, client
from config import OWNER_ID
from bot import bot

scheduler = AsyncIOScheduler()

async def send_news():
    """Собираем посты с всех каналов в один дайджест и отправляем владельцу"""
    posts = await collect_posts(limit=15)

    if not posts:
        await bot.send_message(OWNER_ID, "Сегодня новых новостей нет.")
        return

    # Группируем посты по каналам
    from collections import defaultdict
    channel_posts = defaultdict(list)
    for p in posts:
        channel_posts[p['channel']].append(p['text'][:200])  # обрезаем текст для краткости

    # Формируем дайджест
    digest = "📰 *Новости за сегодня:*\n\n"
    for channel, msgs in channel_posts.items():
        digest += f"📌 *{channel}*\n"
        for msg in msgs:
            digest += f"- {msg}\n"
        digest += "\n"
        await asyncio.sleep(1)  # небольшая пауза между каналами

    # Отправляем одним сообщением
    await bot.send_message(OWNER_ID, digest, parse_mode="Markdown")

def setup_scheduler():
    """Запускаем расписание"""
    scheduler.add_job(send_news, "cron", hour=9)   # каждый день 9:00
    scheduler.add_job(send_news, "cron", hour=18)  # каждый день 18:00
    scheduler.start()
