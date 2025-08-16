from fastapi import FastAPI

app = FastAPI(
    title="Orchestration Service",
    description="Manages the lifecycle of security scans.",
    version="0.1.0",
)

@app.get("/health", tags=["Monitoring"])
def health_check():
    """Simple health check endpoint to confirm the service is running."""
    return {"status": "ok"}
