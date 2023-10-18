FROM python:3.10

ENV POETRY_VERSION=1.3.1 \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

RUN apt update

WORKDIR /app/
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false
RUN poetry run pip install -U setuptools==59.1.1
RUN poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /app/

ENTRYPOINT ["python", "main.py"]
