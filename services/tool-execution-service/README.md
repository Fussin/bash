# Tool Execution Service

This service acts as a worker that listens for `TaskRequest` events from Kafka. It is responsible for executing security tools (e.g., nmap, nuclei) in a secure and isolated manner, collecting their raw output, and publishing the results back for processing. It is designed to be horizontally scalable.
