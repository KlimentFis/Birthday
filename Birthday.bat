@echo off
REM Переходим в директорию проекта
cd /d C:\Users\Klime\Desktop\Birthday

REM Активируем виртуальное окружение
call venv\Scripts\activate

REM Запускаем Python-скрипт
python main.py

REM Деактивируем виртуальное окружение (опционально)
deactivate

pause
