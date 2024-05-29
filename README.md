# Ресурс для публикации рецептов
Сайт, на котором пользователи публикуют рецепты, добавляют чужие рецепты в избранное и подписываются на публикации других авторов.Пользователям сайта доступен сервис «Список покупок». Он позволит создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

Ссылка на сайт: https://recipes.hopto.org/recipes

### Стек технологий:
<img src="https://img.shields.io/badge/Python-3776ab?style=for-the-badge&logo=python&logoColor=yellow"/> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/Django Rest framework-092E20?style=for-the-badge&logoColor=white"/> <img src="https://img.shields.io/badge/PostgreSQL-50b0f0?style=for-the-badge&logo=postgresql&logoColor=white"/> <img src="https://img.shields.io/badge/CI&CD-B8860B?style=for-the-badge"/> <img src="https://img.shields.io/badge/github actions-4B0082?style=for-the-badge&logo=githubactions&logoColor=2088FF"/> <img src="https://img.shields.io/badge/docker-1d63ed?style=for-the-badge&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/nginx-006400?style=for-the-badge&logo=nginx&logoColor=32CD32"/> <img src="https://img.shields.io/badge/gunicorn-6B8E23?style=for-the-badge&logo=gunicorn&logoColor=1d692d"/> <img src="https://img.shields.io/badge/JWT-2980b9?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAACVBMVEVGUViMoa/i5+sa4fYGAAAALElEQVQ4y2NgoAtghAMghwkZUFMBgoKJ0l/BqDdpoYCgG+iggA7eJEMBjQEA95EC+R9NCHIAAAAASUVORK5CYII="/> <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=FF4500"/> <img src="https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white"/> <img src="https://img.shields.io/badge/yaml-FF0000?style=for-the-badge&logo=yaml&logoColor=white"/>


### Порядок установки API:

Клонировать репозиторий и перейти в него в командной строке:
```sh
git clone git@github.com:PaShyKDF/Recipes_site.git
```

```sh
cd backend
```

**Cоздать и активировать виртуальное окружение:**

```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```

**Установить зависимости из файла requirements.txt:**

```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

**Выполнить миграции:**

```sh
python3 manage.py migrate
```

**Запустить проект:**

```sh
python3 manage.py runserver
```

### Запуск на сайта:

**Создать файл .env в корне проекта и записать данные для подлючения к базе данных и настроек settings.py**
```.env
POSTGRES_USER=django_user
POSTGRES_PASSWORD=password
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
DJANGO_KEY='django_key'
DEBUG_VALUE='True'
ALLOWED_HOSTS='site1,site2,site3'
```
**Запустить сборку проета**
```bash
sudo docker compose -f docker-compose.production.yml up
```

### Примеры запросов к API:

**Создание пользователя**

POST ```https://yapract-foodgram.hopto.org/api/users/```

Данные запроса:
```json
{
    "email": "vpupkin@yandex.ru",
    "username": "vasya.pupkin",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "password": "Qwerty123"
}
```
Ответ:
```json
{
    "email": "vpupkin@yandex.ru",
    "id": 0,
    "username": "vasya.pupkin",
    "first_name": "Вася",
    "last_name": "Пупкин"
}
```
**Получение токена**

POST ```https://yapract-foodgram.hopto.org/api/auth/token/login/```

Данные запроса:
```json
{
    "password": "string",
    "email": "string"
}
```
Ответ:
```json
{
    "auth_token": "string"
}
```
**Получение рецептов**

GET ```https://yapract-foodgram.hopto.org/api/recipes/```

Ответ:
```json
{
  "count": 123,
  "next": "http://foodgram.example.org/api/recipes/?page=4",
  "previous": "http://foodgram.example.org/api/recipes/?page=2",
  "results": [
    {
      "id": 0,
      "tags": [
        {
          "id": 0,
          "name": "Завтрак",
          "color": "#E26C2D",
          "slug": "breakfast"
        }
      ],
      "author": {
        "email": "user@example.com",
        "id": 0,
        "username": "string",
        "first_name": "Вася",
        "last_name": "Пупкин",
        "is_subscribed": false
      },
      "ingredients": [
        {
          "id": 0,
          "name": "Картофель отварной",
          "measurement_unit": "г",
          "amount": 1
        }
      ],
      "is_favorited": true,
      "is_in_shopping_cart": true,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "text": "string",
      "cooking_time": 1
    }
  ]
}
```
**Создание рецепра**

POST ```https://yapract-foodgram.hopto.org/api/recipes/```

Данные запроса:
```json
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
```
Ответ:
```json
{
  "id": 0,
  "tags": [
    {
      "id": 0,
      "name": "Завтрак",
      "color": "#E26C2D",
      "slug": "breakfast"
    }
  ],
  "author": {
    "email": "user@example.com",
    "id": 0,
    "username": "string",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "is_subscribed": false
  },
  "ingredients": [
    {
      "id": 0,
      "name": "Картофель отварной",
      "measurement_unit": "г",
      "amount": 1
    }
  ],
  "is_favorited": true,
  "is_in_shopping_cart": true,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "text": "string",
  "cooking_time": 1
}
```
**Добавить рецепт в список покупок**

POST/DELETE ```https://yapract-foodgram.hopto.org/api/recipes/{id}/shopping_cart/```

Ответ:
```json
{
    "id": 0,
    "name": "string",
    "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
    "cooking_time": 1
}
```
**Скачать список покупок**

GET ```https://yapract-foodgram.hopto.org/api/recipes/download_shopping_cart/```

**Добавить рецепт в избранное**

POST/DELETE ```https://yapract-foodgram.hopto.org/api/recipes/{id}/favorite/```

Ответ:
```json
{
    "id": 0,
    "name": "string",
    "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
    "cooking_time": 1
}
```
**Мои подписки**

GET ```https://yapract-foodgram.hopto.org/api/users/subsciptions```

Ответ:
```json
{
  "count": 123,
  "next": "http://foodgram.example.org/api/users/subscriptions/?page=4",
  "previous": "http://foodgram.example.org/api/users/subscriptions/?page=2",
  "results": [
    {
      "email": "user@example.com",
      "id": 0,
      "username": "string",
      "first_name": "Вася",
      "last_name": "Пупкин",
      "is_subscribed": true,
      "recipes": [
        {
          "id": 0,
          "name": "string",
          "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
          "cooking_time": 1
        }
      ],
      "recipes_count": 0
    }
  ]
}
```
**Подписаться на пользователя**

POST/DELETE ```https://yapract-foodgram.hopto.org/api/recipes/{id}/subscribe/```

Ответ:
```json 
{
  "email": "user@example.com",
  "id": 0,
  "username": "string",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "is_subscribed": true,
  "recipes": [
    {
      "id": 0,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "cooking_time": 1
    }
  ],
  "recipes_count": 0
}
```
**Список ингредиентов**

GET ```https://yapract-foodgram.hopto.org/api/ingredients/```

Ответ:
```json
[
  {
    "id": 0,
    "name": "Капуста",
    "measurement_unit": "кг"
  }
]
```

Ссылка на сайт: ```https://yapract-foodgram.hopto.org/```  
Почта адина: ```admin@ad.ru```  
Пароль от админки: ```12341234```