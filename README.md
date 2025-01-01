# Авто поздравления с Днем Рождения!🥳🥳🥳

![](https://avatars.mds.yandex.net/i?id=d7e7a78150ce9795a9483c1bc1e0f98f_l-9097903-images-thumbs&n=13)

## Подготовка
Зайдите на [сайт](https://my.telegram.org), и вставьте в файл [config.py](config.py) `api_id`, `api_hash`.

## Установка

### Клонирование и переход в папку проекта:
```bash
git clone https://github.com/KlimentFis/Birthday.git && cd Birthday
```

### Создание виртуального окружения:
```bash
python -m venv venv
```

### Активация виртуального окружения:
```bash
venv\Scripts\activate
```

### Установка зависимостей:
```bash
pip install -r req.txt
```

## Запуск проекта
```bash
python main.py
```

## Как узнать id пользователя

### С помощью уже установленной библиотеки:
```python
from pyrogram import Client
from config import api_id, api_hash

# Создание клиента
app = Client(
    "my_account",  # Имя сессии
    api_id=api_id,
    api_hash=api_hash
)

with app:
    user = app.get_users("Ник_Пользователя")
    print(user)
```

### С помощью сторонней библиотеки:

#### Установка библиотеки:
```bash
pip install telethon
```

#### Поиск данных о пользователе по номеру:
```python
from telethon.sync import TelegramClient
from config import api_id, api_hash 

# Ваши данные для подключения
api_id = api_id  # Введите свой API ID
api_hash = api_hash  # Введите свой API Hash
phone_number = ''  # Замените на нужный номер телефона

# Создание клиента
client = TelegramClient('session_name', api_id, api_hash)

async def get_user_id():
    # Получаем информацию о пользователе по номеру телефона
    user = await client.get_entity(phone_number)
    print(f"User ID: {user.id}")

# Запуск клиента
client.start()
client.loop.run_until_complete(get_user_id())
```

## Автоматизация

Закиньте [файл](Birthday.bat) в папку Автозагрузки, и пропишите в нем правильный путь до папки с проектом:
```bat
@echo off
REM Переходим в директорию проекта
cd C:\Users\Klime\My_dir\Projects\Birthday

REM Активируем виртуальное окружение
call venv\Scripts\activate

REM Запускаем Python-скрипт
python main.py

REM Деактивируем виртуальное окружение (опционально)
deactivate

pause
