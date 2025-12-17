## Тестовое задание "Сервис для хранения ссылок".

### Описание:

Сервис для хранения ссылок, парсинга их основной информации.  
Для сохранения метаинформации о ссылке используется парсинг OG-тегов.  
Подробнее в OG-тегах: <https://ogp.me/>

### Стек:

- `Django REST Framework`
- `BeautifulSoup`
- `httpx`
- `pydantic-settings`
- `drf-spectacular`
- `PostgreSQL`
- `Docker`

### Установка зависимостей:

1. Создать окружение через `poetry`.

2. Установить только основные зависимости, необходимые для запуска:
   ```shell
   poetry install --no-root --without dev
   ```

3. Установить все зависимости, включая `dev`/`test` (+linter, +pre-commit и т.д.):
    ```shell
    poetry install --no-root
    ```

### Pre-commit, Linter, Formatter:

- Установить `pre-commit` хуки:
    ```shell
    pre-commit install
    ```

- Ручной запуск линтера и форматера:
    ```shell
    ruff check && ruff format
    ```

### Запуск:

1. Создать файл `.env` по примеру `example.env`.

2. Основные команды запуска смотрите в `Makefile`:
    ```shell
    make up
    ```
