from fastapi import FastAPI

app = FastAPI(
    title="Data Processing Service",
    description="A service that parses and standardizes raw tool output.",
    version="0.1.0",
)

@app.get("/health", tags=["Monitoring"])
def health_check():
    """Simple health check endpoint to confirm the service is running."""
    return {"status": "ok"}

# The main worker logic will be started in a separate thread or process.
# It will consume from a Kafka topic, parse the data, and produce to another topic.
