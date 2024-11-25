# Авто поздравления с Днем Рождения! 🥳🥳🥳

![](https://avatars.mds.yandex.net/i?id=d7e7a78150ce9795a9483c1bc1e0f98f_l-9097903-images-thumbs&n=13)

### Подготовка
Зайдите на [сайт](https://my.telegram.org), и вставьте в файл [config.py](config.py) api_id, api_hash

### Установка
Клонирование и переход в папку проекта:
``` 
git clone https://github.com/KlimentFis/Birthday.git && cd Birthday
```
Создание виртуального окружения:
``` 
python -m venv venv
```
Активация виртуального окружения:
``` 
venv\Scripts\activate
```
Установка зависимостей:
``` 
pip install -r req.txt
```
Запуск:
``` 
python main.py
```

### Как узнать id пользователя
```
from pyrogram import Client

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