# Data Processing Service

This service consumes raw tool output from a Kafka topic. Its primary role is to parse this varied data into a standardized, structured format (e.g., a "Finding" document). It may use a variety of parsers, and in the future, potentially LLMs for handling unstructured data. The processed data is then sent to the Persistence Service.
