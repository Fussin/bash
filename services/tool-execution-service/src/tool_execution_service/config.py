# Configuration for the Tool Execution Service
import os

KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")
TASK_REQUEST_TOPIC = "task.request.v1"
RESULT_INFORM_TOPIC = "result.inform.v1"
