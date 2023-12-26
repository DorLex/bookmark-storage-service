## Сервис для хранения закладок

### Запуск проекта:

#### 1. Клонировать репозиторий:

```bash
git clone git@github.com:DorLex/bookmark-storage-service.git
```

#### 2. Перейдя в корневую папку проекта, создать файл `.env` (как в примере `.env.example`).

#### 3. Сбилдить через docker compose:

```bash
docker compose build
```

#### 4. Запустить:

```bash
docker compose up
```

#### 5. Произвести миграции:

```bash
 docker compose run --rm app python manage.py migrate
```

#### 6. Создать суперпользователя:

```bash
docker compose run --rm app python manage.py createsuperuser
```

#### 7. Swagger документация:

http://127.0.0.1:8000/swagger/

#### 8. Если хотим прогнать тесты:

```bash
docker compose run --rm app python manage.py test
```
