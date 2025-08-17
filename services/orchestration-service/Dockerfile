# syntax=docker/dockerfile:1

# 1. Builder stage: Install dependencies
FROM python:3.11-slim as builder
WORKDIR /app
RUN pip install poetry
COPY services/orchestration-service/pyproject.toml services/orchestration-service/poetry.lock* ./
# Install dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# 2. Final stage: Create the runtime image
FROM python:3.11-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /app /app

# Copy the application source code
COPY services/orchestration-service/src/ ./src/

# Create a non-root user for security
RUN useradd --create-home appuser
USER appuser

# This service runs the MCP client, which is a long-running script.
# It connects to the tool-execution-service.
CMD ["poetry", "run", "python", "src/orchestration_service/chimera_mcp.py"]
