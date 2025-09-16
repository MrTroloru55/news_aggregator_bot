# scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from collector import collect_posts
from config import OWNER_ID
import asyncio
from aiogram import Bot
from collections import defaultdict

scheduler = AsyncIOScheduler()

# Определяем черный список
BLACKLIST = ['@concertzaal']

def remove_blacklist_words(text: str) -> str:
    """Удаляет слова из черного списка."""
    if not text:
        return ""
    for word in BLACKLIST:
        text = text.replace(word, '').strip()
    return text

async def send_news(bot: Bot):
    print("Начинаю сбор новостей...")
    posts = await collect_posts(limit=3)

    if not posts:
        await bot.send_message(OWNER_ID, "Сегодня новых новостей нет.")
        print("Новых постов не найдено.")
        return

    print(f"Найдено {len(posts)} постов. Начинаю отправку...")

    # Группируем посты по каналам
    channel_posts = defaultdict(list)
    for p in posts:
        # Применяем фильтр черного списка
        p['text'] = remove_blacklist_words(p['text'])
        channel_posts[p['channel']].append(p)
    
    # Отправляем дайджест для каждого канала
    for channel, posts_list in channel_posts.items():
        digest = f"📌 *{channel}*\n\n"
        current_digest_length = len(digest)
        
        for post in posts_list:
            # Добавляем разделитель перед каждым постом, кроме первого
            if len(digest.strip()) > 0:
                text_to_add = "-------------------\n"
            else:
                text_to_add = ""

            text_to_add += f"- {post['text']}\n"
            if len(text_to_add.strip()) > 0:
                text_to_add += "\n"

            if current_digest_length + len(text_to_add) > 4000:
                await bot.send_message(OWNER_ID, digest, parse_mode="Markdown")
                await asyncio.sleep(1)
                digest = f"📌 *{channel}* (продолжение)\n\n"
                current_digest_length = len(digest)

            digest += text_to_add
            current_digest_length += len(text_to_add)

        if len(digest.strip()) > 0:
            await bot.send_message(OWNER_ID, digest, parse_mode="Markdown")
            await asyncio.sleep(1)

    print("Все новости успешно отправлены.")
            
def setup_scheduler(bot: Bot):
    scheduler.add_job(send_news, "interval", minutes=2, args=[bot])
    scheduler.start()