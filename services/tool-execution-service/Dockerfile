# syntax=docker/dockerfile:1

# 1. Builder stage: Install dependencies
FROM python:3.11-slim as builder
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock* ./
# Install dependencies, excluding dev ones
RUN poetry install --no-dev --no-interaction --no-ansi

# 2. Final stage: Create the runtime image
FROM python:3.11-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /app /app

# Copy the application source code
COPY src/ ./src/

# Create a non-root user for security
RUN useradd --create-home appuser
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "tool_execution_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
