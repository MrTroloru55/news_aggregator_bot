# config.py
# Хранение токенов и настроек
import os

with open('/home/dima/paperboy_3/paperboy/token_paperboy.txt', 'r') as file:
    BOT_TOKEN = file.readline().strip()
    
with open('/home/dima/paperboy_3/paperboy/API_ID_paperboy.txt', 'r') as file:
    API_ID = file.readline().strip()
    
with open('/home/dima/paperboy_3/paperboy/API_HASH_paperboy.txt', 'r') as file:
    API_HASH = file.readline().strip()

#with open('C:\\Users\\user\\Desktop\\paperboy\\OWNER_ID_paperboy.txt', 'r') as file:
#    OWNER_ID = file.readline().strip()

OWNER_ID = 683852062
#POST_LIMIT = 10
SESSION_NAME = "paperboy_bot"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "Data_base", "main.db")
print(f"Путь к базе данных: {DB_PATH}")
