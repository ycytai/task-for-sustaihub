FROM python:3.10-slim

ENV POETRY_VERSION=1.4.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
  && poetry install

COPY . /code
