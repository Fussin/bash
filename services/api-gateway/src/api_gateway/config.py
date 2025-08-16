# Configuration for the API Gateway
import os

# Address of the orchestration service, which the gateway will call
ORCHESTRATION_SERVICE_URL = os.getenv("ORCHESTRATION_SERVICE_URL", "http://orchestration-service:8000")
