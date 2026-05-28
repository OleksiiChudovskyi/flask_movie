# Flask Movie API

Потужне, масштабоване та повністю RESTful API для керування базою даних фільмів та акторів. Проєкт розроблено на базі Flask із дотриманням сучасних практик веб-розробки, суворої ізоляції залежностей, контейнеризації та автоматичного тестування. Він забезпечує швидку інтеграцію, легке масштабування та високу безпеку даних.
## 📊 Status of Workflows

[![Tests in Docker](https://github.com/OleksiiChudovskyi/flask_movie/actions/workflows/tests_docker.yml/badge.svg?branch=main)](https://github.com/OleksiiChudovskyi/flask_movie/actions/)
[![Tests in VM](https://github.com/OleksiiChudovskyi/flask_movie/actions/workflows/tests_vm.yml/badge.svg?branch=main)](https://github.com/OleksiiChudovskyi/flask_movie/actions/)

---

## 📝 Веріся Репозиторія & Відкритиість Коду

Цей репозиторій створено з метою максимально прозорої демонстрації архітектури проєкту та навичок розробки.

- **Повний вихідний код:** На [GitHub-репозиторії Flask Movie API](https://github.com/OleksiiChudovskyi/flask_movie) опубліковано весь відкритий код, архітектурну структуру, а також конфігураційні файли й папки, які зазвичай додаються до файлів `.gitignore` та `.dockerignore`.  
    Це зроблено навмисно, щоб ви могли детально ознайомитися з повним циклом розробки проекту.
- **Безпека даних:** Для запобігання витоку будь-якої чутливої інформації (приватні API-ключі, токени автентифікації, паролі до баз даних) з цієї версії репозиторія було повністю видалено історію попередніх комітів.  
    Усі поточні конфігураційні файли містять лише безпечні демонстраційні значення.

---

## 🌐 Живе демо (Production)

Проєкт розгорнуто та запущено в продакшен-середовищі на Railway. Ви можете ознайомитися з інтерактивною документацією та протестувати роботу API за посиланням:
👉 **[Production version Flask Movie API](https://movie-flask.up.railway.app/api/v1/swagger/)**

---

## 🚀 Особливості проєкту

* **Сучасний стек**: Базується на Python 3.11, Flask-RESTful та Marshmallow для чистої серіалізації.
* **Керування даними**: Повноцінна ORM SQLAlchemy (PostgreSQL) та автоматичні міграції через Flask-Migrate (Alembic).
* **Ізоляція середовищ**: Окремі Docker-конфігурації для розробки, тестування та стабільного продакшену.
* **Безпека**: Генерація та валідація JWT-токенів (PyJWT), а також захист паролів через Docker Secrets.
* **Документація**: Інтегрована Swagger UI для візуального тестування ендпоінтів у реальному часі.
* **Контроль якості**: Покриття коду тестами (Pytest, Coverage, Mock) та автоматична перевірка стилю (Flake8).

---

## 🛠️ Технологічний стек

* **Framework**: Flask, Flask-RESTful
* **Database & ORM**: PostgreSQL, Flask-SQLAlchemy, Flask-Migrate
* **Package Manager**: Poetry
* **Security & Tools**: PyJWT, BeautifulSoup4 (bs4), Requests
* **WSGI & Server**: Gunicorn, NGINX
* **DevOps**: Docker, Docker Compose

---

## 📦 Встановлення та налаштування локально

Переконайтеся, що у вас встановлено **Python 3.11** та **Poetry**.

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com
   cd flask_movie
   ```

2. Встановіть залежності через Poetry:
   ```bash
   poetry install
   ```

3. Активуйте віртуальне середовище:
   ```bash
   poetry shell
   ```

---

## 🐳 Запуск через Docker Compose

Проєкт підтримує три готові сценарії Docker для різних етапів розробки:

### 1. Розробка (Development)
Використовує механізм `Deploy and watch` для миттєвого оновлення контейнерів під час редагування коду:
```bash
docker compose -f compose.dev.yml up --build
```

### 2. Тестування (Testing)
Запускає тести всередині контейнера через `Pytest`, використовуючи швидку базу даних `sqlite3:memory:`, та автоматично створює звіт `coverage`:
```bash
docker compose -f compose.test.yml up --build
```

### 3. Продакшен (Production)
Запускає стійку до навантажень архітектуру. Застосунок працює через `Gunicorn`, запити проксуються через `NGINX`, а паролі та ключі надійно захищені за допомогою `Docker Secrets`:
```bash
docker compose -f compose.prod.yml up -d --build
```

---

## 📈 Тестування та якість коду

Для запуску перевірок локально (без Docker) використовуйте наступні команди:

```bash
# Запуск тестів та аналіз покриття коду
poetry run pytest --cov=src

# Перевірка відповідності коду стандарту PEP 8
poetry run flake8 src
```

---

## 🗺️ Короткий огляд API Ендпоінтів

Після запуску проєкту інтерактивна документація **Swagger UI** доступна за адресою: `http://localhost:5000/swagger` *(або на порту, який вказано у ваших налаштуваннях)*.

### Фільми (Movies)
* `GET /movies` — Отримати список усіх фільмів.
* `POST /movies` — Додати новий фільм.
* `GET /movies/<id>` — Отримати деталі конкретного фільму.
* `PUT /movies/<id>` — Оновити інформацію про фільм.
* `DELETE /movies/<id>` — Видалити фільм.

### Актори (Actors)
* `GET /actors` — Отримати список усіх акторів.
* `POST /actors` — Додати нового актора.
* `GET /actors/<id>` — Отримати деталі конкретного актора.
* `PUT /actors/<id>` — Оновити інформацію про актора.
* `DELETE /actors/<id>` — Видалити актора.

---

## 👥 Автор

* **Oleksii Chudovskyi** — [oleksii.chudovskyi@gmail.com](mailto:oleksii.chudovskyi@gmail.com)