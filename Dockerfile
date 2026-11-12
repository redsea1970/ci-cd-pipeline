FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml requirements-dev.txt ./
COPY src ./src
RUN pip install --no-cache-dir -e . && pip install --no-cache-dir pytest
EXPOSE 8000
CMD ["python", "-c", "from app.main import health; print(health())"]
