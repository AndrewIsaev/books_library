# Books library
Simple books library
***
## Features
- Registration/Authentication
- Books
  - Pagination for books list
  - Creating/changing/deleting books
  - Add comments for book
- Search books by title or author name
- API for list and detail books
***
## Technology stack
- Python 3.11
- Django 4.2.5
- Django REST Framework 3.14.0
- Poetry 1.5.1
- PostgreSQL
- Docker
- Docker-compose
- pre-commit
- black
- flake8
- mypy
- isort
***
## Start app
1. Create .env file:
   ```
   POSTGRES_PASSWORD=
   POSTGRES_USER=
   POSTGRES_DB=
   PGUSER=

   DB_USER=
   DB_PASSWORD=
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=books_library


   SECRET_KEY=""
   DEBUG=
2. Run docker container
   ```
    docker-compose up --build
***
## Project structure
- `api/`: API for books list and detail
- `core/`: login/register application
- `books/`: books application
- `books_library/`: Django settings
- `.env`: environment variables
- `.pre-commit-config.yaml`: pre-commit settings
- `Dockerfile`: docker file
- `docker-compose.yaml`: docker compose file
- `poetry.lock`: packages dependencies
- `pyproject.toml`: packages list
- `manage.py`: Django app management
