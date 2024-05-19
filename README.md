# Telegram Bot для агрегации данных о зарплатах

Этот Telegram бот предназначен для агрегации данных о зарплатах из MongoDB на основе заданных временных интервалов. Бот построен с использованием `aiogram`, `motor` и других современных Python-библиотек. Приложение контейнеризовано с использованием Docker для упрощения развертывания.

## Содержание

- [Особенности](#особенности)
- [Используемые технологии](#используемые-технологии)
- [Настройка и установка](#настройка-и-установка)
- [Запуск проекта](#запуск-проекта)
- [Использование](#использование)
- [Структура проекта](#структура-проекта)
- [Лицензия](#лицензия)

## Особенности

- Агрегация данных о зарплатах на основе часовых, дневных или месячных интервалов.
- Использование MongoDB для хранения данных.
- Кэширование результатов агрегации для повышения производительности.
- Использование Docker для контейнеризации и упрощения развертывания.
- Включение middleware для предотвращения спама.

## Используемые технологии

- Python 3.11
- aiogram 3.6.0
- motor 3.4.0
- aiocache 0.12.2
- MongoDB
- Docker & Docker Compose
- Poetry для управления зависимостями

## Настройка и установка

### Предварительные требования

- Установленные Docker и Docker Compose на вашем компьютере
- Установленный Poetry (необязательно, для локальной разработки)

### Шаги установки

1. **Клонирование репозитория:**
    ```sh
    git clone https://github.com/Keni13-coder/bot-for-test.git
    cd telegram-salary-aggregation-bot
    ```

2. **Создание файла `.env` с вашим токеном бота и URI MongoDB:**
    ```sh
    touch .env
    echo "BOT_TOKEN=your_telegram_bot_token" >> .env
    echo "MONGO_URI=mongodb://mongodb:27017" >> .env
    echo "MONGO_DB=your_database_name" >> .env
    echo "RATE_LIMIT_MESSAGE=5" >> .env
    ```

3. **Сборка и запуск Docker контейнеров:**
    ```sh
    docker-compose up --build
    ```

## Запуск проекта

После настройки и установки проекта, вы можете запустить его с помощью Docker Compose. Команда ниже запустит как сервисы MongoDB, так и бота:

```sh
docker-compose up --build
