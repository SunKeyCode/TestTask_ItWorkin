# Тестовое задание для компании IT Working

## Задача
Написать RESTful API простого мессенджера.


### Реализуемый функционал:

- Механизм авторизации

- Поиск пользователей

- Возможность отправлять личные сообщения

- Настройки пользователя (username, аватар, номер телефона, т.п.)

## Стек технологий:

- fastapi
- sqlalchemy
- sqlite
- alembic


## Установка 

- скачать репозиторий
- установить poetry
- перейти в папку с проектом
- poetry install
- poetry shell
- cd backend/app
- alembic upgrade head
- переименовать .env.template в .env
- uvicorn main:app (по умолчанию запускается на localhost:8000)