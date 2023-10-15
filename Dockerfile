FROM python:3.11-slim

# Устанавливаем переменную окружения для отключения режима вывода Python в буфер
ENV PYTHONUNBUFFERED 1

# Создаем и переходим в рабочий каталог /app
WORKDIR /app

# Копируем файл зависимостей (pyproject.toml и poetry.lock) в рабочий каталог
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry
RUN pip install poetry
# Устанавливаем зависимости
RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-root

# Копируем все файлы приложения в рабочий каталог
COPY . /app/

# Открываем порт, на котором будет работать приложение (замените 8000 на порт вашего приложения)
EXPOSE 8000

# Запускаем команду для запуска вашего приложения (здесь предполагается, что ваше приложение запускается с помощью gunicorn)
CMD ["python", "manage.py", "runserver"]
