{Структура

news_bot/
│── main.py          # Точка входа (запуск бота и планировщика)
│── config.py        # Конфиги: токены, api_id, api_hash
│── db.py            # Работа с SQLite
│── bot.py           # Логика aiogram (команды и хендлеры)
│── collector.py     # Логика Telethon для сбора постов
│── scheduler.py     # Планировщик заданий (apscheduler)
│── requirements.txt # Зависимости

}