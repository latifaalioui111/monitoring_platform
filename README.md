# Security-Aware Monitoring Platform

A platform that monitors the availability and security posture of web services,
automatically detects incidents, and generates AI-powered incident analysis.

## Features
- Service monitoring: HTTP(S), TCP, SSL/TLS certificates
- Domain ownership verification before any check (DNS TXT record)
- Time-series storage and anomaly detection
- Automatic incident creation and email alerts
- LLM-generated incident summaries, with prompt injection protection

## Architecture
Microservices architecture with asynchronous, event-driven communication (AWS SQS/SNS).

| Database | Role |
| PostgreSQL | Users and monitor configuration |
| MongoDB | Incidents and AI-generated reports |
| HBase | Time-series metrics |

## Tech Stack
Python (FastAPI), Docker, Kubernetes, Terraform, AWS, GitHub Actions

## Security (DevSecOps)
Secret, code, dependency, image and infrastructure scanning in the CI/CD pipeline,
with image signing and Kubernetes policies.

