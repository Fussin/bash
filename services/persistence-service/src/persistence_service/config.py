# Configuration for the Persistence Service
import os

# PostgreSQL connection string
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"

# MongoDB connection string
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:27017/"

KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "kafka:9092")
PERSISTENCE_QUEUE_TOPIC = "persistence.queue.v1"
