# Persistence Service

This service provides a centralized interface for all data persistence operations. It abstracts the underlying databases (PostgreSQL for relational data, MongoDB for documents) from the other services. It consumes structured data from a Kafka topic and writes it to the appropriate database. It may also expose an internal API for complex queries if needed.
