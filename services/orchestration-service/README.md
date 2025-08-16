# Orchestration Service

This service is responsible for managing the lifecycle of security scans. It uses a Finite-State Machine (FSM) to track scan progress, dispatches tasks to worker agents via Kafka, and persists high-level scan state.
