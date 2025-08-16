from fastapi import FastAPI

app = FastAPI(
    title="Persistence Service",
    description="A service that abstracts database operations.",
    version="0.1.0",
)

@app.get("/health", tags=["Monitoring"])
def health_check():
    """Simple health check endpoint to confirm the service is running."""
    return {"status": "ok"}

# The main worker logic will be started in a separate thread or process.
# It will consume from a Kafka topic and write to the databases.
# It may also include API endpoints for querying data.
