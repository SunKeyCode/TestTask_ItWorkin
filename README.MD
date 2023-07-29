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

**Ссылка на OpenApi документацию** -
localhost:8000/docs

**urls:**

- /auth/register - регистрация пользователя
- /auth/login - вход по username и password
- /auth/me/update - обновить профиль пользователя
- /auth/me/ - получить профиль пользователя
- /api/v1/messages/send - отправить личное сообщение
- /api/v1/messages/get_undelivered - получить непрочитанные сообщения
- /api/v1/messages/delivered - сделать сообщение прочитанным
- /api/v1/users/search - поиск пользователя по части username
- /api/v1/media/avatar/create - cоздание/изменение аватара

Используется bearer token аутентификация, для получения доступа к эндпоинту необходимо отправлять заголовок
Authorization: bearer token (token получаем от /auth/login)


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