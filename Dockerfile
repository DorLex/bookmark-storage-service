FROM python:3.11.7-alpine3.19

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV PATH=/root/.local/bin:$PATH


RUN apk --no-cache add curl

RUN curl -sSL https://install.python-poetry.org | python3.11 -

RUN poetry config virtualenvs.create false


WORKDIR /project

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .


EXPOSE 8000
