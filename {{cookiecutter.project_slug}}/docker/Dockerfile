FROM python:3.12.2-alpine3.19 AS build

WORKDIR /staging

RUN pip install --no-cache-dir poetry

COPY pyproject.toml ./

RUN POETRY_VIRTUALENVS_IN_PROJECT=true poetry install --only main --no-root



FROM python:3.12.2-alpine3.19 AS runtime

RUN apk update && \
    apk upgrade && \
    apk add --no-cache curl

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser
USER appuser

COPY --chown=appuser --from=build /staging/.venv/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --chown=appuser src/. .

EXPOSE 8000
CMD ["python", "main.py"]
