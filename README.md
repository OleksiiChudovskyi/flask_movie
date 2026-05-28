# Flask Movie API

Потужне, масштабоване та повністю **RESTful API** для керування базою даних фільмів та акторів. 
Проєкт розроблено на базі **Flask** із дотриманням сучасних практик веб-розробки, суворої ізоляції залежностей, контейнеризації та автоматичного тестування. 
Він забезпечує швидку інтеграцію, легке масштабування та високу безпеку даних.

## 📊 Status of Workflows

[![Tests in Docker](https://github.com/OleksiiChudovskyi/flask_movie/actions/workflows/tests_docker.yml/badge.svg?branch=main)](https://github.com/OleksiiChudovskyi/flask_movie/actions/)
[![Tests in VM](https://github.com/OleksiiChudovskyi/flask_movie/actions/workflows/tests_vm.yml/badge.svg?branch=main)](https://github.com/OleksiiChudovskyi/flask_movie/actions/)

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
* **Якість коду та CI/CD:** Автоматизовані процеси через GitHub Actions, що включають тестування, а також лінтинг і форматування за допомогою `Ruff`.

---

## 🛠️ Технологічний стек

* **Language**: Python 3.11+
* **Framework**: Flask, Flask-RESTful
* **Validation**: Marshmallow
* **Database & ORM**: PostgreSQL, Flask-SQLAlchemy, Flask-Migrate, Alembic
* **Package Manager**: Poetry
* **Security & Tools**: PyJWT, BeautifulSoup4 (bs4), Requests
* **WSGI & Server**: Gunicorn, NGINX
* **DevOps**: Docker, Docker Compose

---

## 📝 Веріся Репозиторія & Відкритиість Коду

Цей репозиторій створено з метою максимально прозорої демонстрації архітектури проєкту та навичок розробки.

- **Повний вихідний код:** На [GitHub-репозиторії Flask Movie API](https://github.com/OleksiiChudovskyi/flask_movie) опубліковано весь відкритий код, архітектурну структуру, а також конфігураційні файли й папки, які зазвичай додаються до файлів `.gitignore` та `.dockerignore`.  
    Це зроблено навмисно, щоб ви могли детально ознайомитися з повним циклом розробки проекту.
- **Безпека даних:** Для запобігання витоку будь-якої чутливої інформації (приватні API-ключі, токени автентифікації, паролі до баз даних) з цієї версії репозиторія було повністю видалено історію попередніх комітів.  
    Усі поточні конфігураційні файли містять лише безпечні демонстраційні значення.

---

## 📦 Встановлення та налаштування локально

Переконайтеся, що у вас встановлено **Python 3.11** та **Poetry**.

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/OleksiiChudovskyi/flask_movie.git
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

## 📦 Контейнеризація та Середовища

Проєкт має декілька конфігурацій Docker Compose, адаптованих під різні сценарії використання:

1. **Development:** Підтримує технологію `docker compose watch` для гарячого перезавантаження коду (Hot Reloading) у реальному часі без перезбирання образів.
2. **Testing:** Окремий ізольований запуск тестів на базі `Pytest` та обчислення покриття коду за допомогою `Coverage`.
3. **Production:** Максимально захищена версія з використанням Docker Secrets, оптимізованих образів та зворотного проксі-сервера **NGINX**.

---

## 🐳 Запуск через Docker Compose

Переконайтеся, що на вашому комп'ютері встановлено Git та Docker 
(з Docker Compose v2.22.0+ для підтримки watch-режиму).

Проєкт підтримує три готові сценарії Docker для різних етапів розробки:

### 1. Development
Використовує механізм `Deploy and watch` для миттєвого оновлення контейнерів під час редагування коду:
```bash
docker compose -f compose.dev.yml up --build --watch
```

### 2. Testing
Запускає тести всередині контейнера через `Pytest`, використовуючи швидку базу даних `sqlite3:memory:`, та автоматично створює звіт `coverage`:
```bash
docker compose -f compose.test.yml up --build
```

### 3. Production
Запускає стійку до навантажень архітектуру. 
Застосунок працює через `Gunicorn`, запити проксуються через `NGINX`, 
а паролі та ключі надійно захищені за допомогою `Docker Secrets`:

Перед запуском Docker Compose обов'язково експортуйте змінні середовища у поточну сесію термінала за допомогою скрипта встановлення:
```bash
source ./sets/set_env.sh
```

Запустіть контейнери у фоновому фоні (detached mode). 
Процес автоматичного збирання образів оптимізовано для мінімального розміру та максимальної безпеки:
```bash
docker compose -f compose.prod.yml up -d --build
```
**Під час запуску контейнерів автоматично відбудеться:**
1. Очікування готовності бази даних PostgreSQL.
2. Автоматичне застосування всіх міграцій Alembic.
3. Автоматичне наповнення бази даних початковими/тестовими даними (Seeding).
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

Після запуску проєкту інтерактивна документація **Swagger UI** доступна за адресою: `http://localhost:8001/api/v1/swagger/`.

### Films
* `GET /films` — Отримати список усіх фільмів.
* `POST /films` — Додати новий фільм.
* `GET /films/{uuid}` — Отримати деталі конкретного фільму.
* `PUT /films/{uuid}` — Оновити інформацію про фільм.
* `PATCH /films/{uuid}` — Оновити інформацію про фільм.
* `DELETE /films/{uuid}` — Видалити фільм.

### Actors
* `GET /actors` — Отримати список усіх акторів.
* `POST /actors` — Додати нового актора.
* `GET /actors/{uuid}` — Отримати деталі конкретного актора.
* `PUT /actors/{uuid}` — Оновити інформацію про актора.
* `PATCH /actors/{uuid}` — Оновити інформацію про актора.
* `DELETE /actors/{uuid}` — Видалити актора.

---

## 📝 Ліцензія

Цей проєкт є відкритим і поширюється за ліцензією [MIT License](LICENSE).

---

## 👥 Автор

* **Oleksii Chudovskyi** — [oleksii.chudovskyi@gmail.com](mailto:oleksii.chudovskyi@gmail.com)