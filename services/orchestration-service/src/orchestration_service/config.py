# Configuration for the Orchestration Service
# (e.g., database connection strings, Kafka topics)
import os

KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")
