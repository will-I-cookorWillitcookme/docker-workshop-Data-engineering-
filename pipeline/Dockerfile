FROM python:3.13.11-slim

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pipeline.py .
COPY pyproject.toml .python-version uv.lock ./
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

RUN uv sync --locked
ENV PATH="/code/.venv/bin:$PATH"

ENTRYPOINT ["python", "pipeline.py"]