from fastapi import FastAPI

app = FastAPI(
    title="Tool Execution Service",
    description="A worker that executes security tools.",
    version="0.1.0",
)

@app.get("/health", tags=["Monitoring"])
def health_check():
    """Simple health check endpoint to confirm the service is running."""
    return {"status": "ok"}

# The main worker logic will likely be started in a separate thread or process
# or by using a library like `arq` or `celery`.
# For now, the FastAPI app provides a health check.
