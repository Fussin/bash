# syntax=docker/dockerfile:1

# 1. Builder stage: Install dependencies
FROM python:3.11-slim as builder
WORKDIR /app
RUN pip install poetry
COPY services/persistence-service/pyproject.toml services/persistence-service/poetry.lock* ./
# Install dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# 2. Final stage: Create the runtime image
FROM python:3.11-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /app /app

# Copy the application source code
COPY services/persistence-service/src/ ./src/

# Create a non-root user for security
RUN useradd --create-home appuser
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "persistence_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
