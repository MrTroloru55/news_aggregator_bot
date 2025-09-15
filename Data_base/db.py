# db.py
# Модуль для работы с SQLite

import sqlite3
from config import DB_PATH

def init_db():
    """Создаём таблицы, если их нет"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS channels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        link TEXT UNIQUE
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel TEXT,
        message_id INTEGER,
        text TEXT,
        date TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def add_channel(link: str):
    """Добавить канал в базу"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO channels (link) VALUES (?)", (link,))
    conn.commit()
    conn.close()

def get_channels():
    """Получить список каналов"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT link FROM channels")
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]
