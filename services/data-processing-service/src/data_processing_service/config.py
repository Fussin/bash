# Configuration for the Data Processing Service
import os

KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")
RESULT_INFORM_TOPIC = "result.inform.v1"
PERSISTENCE_QUEUE_TOPIC = "persistence.queue.v1" # Example topic to send structured data to
