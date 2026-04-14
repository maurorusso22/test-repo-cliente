FROM python:3.12-slim

ARG MODEL_VERSION=latest

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml .
RUN uv sync --no-dev --no-install-project

COPY src/ src/
COPY scripts/ scripts/

ENV MODEL_VERSION=${MODEL_VERSION}
EXPOSE 8000

CMD ["uv", "run", "python", "-m", "src.predict"]
