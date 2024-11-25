from datetime import datetime
from pyrogram import Client
from random import shuffle
from config import api_id, api_hash

# Создание клиента
app = Client(
    "my_account",  # Имя сессии
    api_id=api_id,
    api_hash=api_hash
)

# Список пользователей с дополнительными данными (ID и дата рождения)
users = {
    "Гуль": {"id": 1, "gender": "ж", "dob": "1990-07-02"},
    "Рус": {"id": 2, "gender": "м", "dob": "1985-08-19"},
    "Рим": {"id": 3, "gender": "ж", "dob": "1992-08-22"},
    "Жек": {"id": 4, "gender": "м", "dob": "1993-07-27"},
    "Дань": {"id": 5, "gender": "м", "dob": "1987-08-14"},
    "Свет": {"id": 6, "gender": "ж", "dob": "1995-09-02"},
    "Артур": {"id": 7, "gender": "м", "dob": "1980-02-10"},
    "Кость": {"id": 8, "gender": "м", "dob": "1998-06-15"},
    "Ян": {"id": 9, "gender": "ж", "dob": "1991-06-30"},
    "Любимая крестная": {"id": 10, "gender": "ж", "dob": "1983-11-10"},
    "Вов": {"id": 11, "gender": "м", "dob": "1992-03-31"},
    "Мам": {"id": 12, "gender": "ж", "dob": "1970-09-23"},
    "Я": {"id": 915938977, "gender": "м", "dob": "2004-09-27"},
    "Валь": {"id": 13, "gender": "ж", "dob": "1994-12-28"},
    "Тань": {"id": 14, "gender": "ж", "dob": "1988-06-19"},
    "Вик": {"id": 15, "gender": "ж", "dob": "1993-01-10"},
    "Алин": {"id": 16, "gender": "ж", "dob": "1990-01-17"},
    "Виолетт": {"id": 17, "gender": "ж", "dob": "1993-01-10"},
    "Тёма": {"id": 18, "gender": "м", "dob": "2000-02-09"},
}

# Шаблоны поздравлений для пользователей
greetings = [
    "{}, поздравляю с Днём Рождения! Пусть будет много ярких моментов и счастливых событий! 🎉",
    "С Днём Рождения, {}! Пусть каждый день будет полон счастья, удачи и приятных сюрпризов! 🌸",
    "Поздравляю с праздником, {}! Пусть твоя жизнь будет наполнена радостью, любовью и теплом! 🌟",
    "{}, поздравляю с этим замечательным днём! Пусть впереди ждёт только лучшее! 🎂",
    "С Днём Рождения, {}! Пусть каждый новый день приносит тебе радость и вдохновение! 🥳",
    "Желаю тебе самых светлых и тёплых дней, {}! Пусть сбудется всё, о чём ты мечтаешь! 💖",
    "С днюхой, {}! Пусть впереди только яркие события, а твоя жизнь будет полна удачи и радости! ✨",
    "С Днём Рождения, {}! Пусть этот день будет только началом новых, счастливых событий в жизни! 🌺",
    "{}, поздравляю! Пусть сбудется всё, о чём ты мечтаешь, и пусть твоя жизнь будет яркой и успешной! 🌈",
    "С Днём Рождения, {}! Пусть этот год принесёт тебе только счастье, радость и море вдохновения! 🌻",
]

# Генерация поздравлений для каждого пользователя
today = datetime.today().strftime('%Y-%m-%d')  # Текущая дата

for name, info in users.items():
    # Проверка, если сегодня день рождения пользователя
    if info["dob"] == today:
        # Перемешиваем шаблоны для каждого имени
        shuffle(greetings)
        
        # Выбираем одно поздравление (например, первое после перемешивания)
        message = greetings[0].format(name)
        
        # Отправка сообщения пользователю через pyrogram
        with app:
            app.send_message(info["id"], message)
            print(f"Сообщение отправлено {name}: {message}")