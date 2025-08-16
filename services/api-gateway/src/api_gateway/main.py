from fastapi import FastAPI

app = FastAPI(
    title="API Gateway",
    description="The single entry point for all external clients.",
    version="0.1.0",
)

@app.get("/health", tags=["Monitoring"])
def health_check():
    """Simple health check endpoint to confirm the service is running."""
    return {"status": "ok"}

# Routers for different API versions or resources will be included here
# e.g., app.include_router(v1_router, prefix="/v1")
