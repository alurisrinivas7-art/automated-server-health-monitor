# Automated Server Health Monitor

A Python-based Linux server monitoring tool that checks CPU, memory, and disk usage and generates structured health reports and webhook alerts when resource utilization exceeds a defined threshold.

## Project Status

Phase 2 — Containerized DevSecOps implementation

## Objectives

- Monitor Linux server health
- Collect CPU, memory, and disk usage
- Detect resource usage above 85%
- Generate structured JSON health reports
- Send notifications through an HTTP webhook
- Containerize the application with Docker
- Automate testing with GitHub Actions
- Build the Docker image automatically in CI
- Scan the Docker image for security vulnerabilities
- Practice Python automation, Linux, Docker, CI/CD, and DevSecOps

## Technology Stack

- Python 3.14
- Linux
- Git & GitHub
- Docker
- GitHub Actions
- pytest
- HTTP / REST
- JSON
- Discord / Slack Webhooks
- Trivy

## Architecture

```text
                    ┌─────────────────────┐
                    │    Linux Server     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Python Health       │
                    │ Monitor             │
                    └──────────┬──────────┘
                               │
                    ┌──────────┼──────────┐
                    ▼          ▼          ▼
                  CPU       Memory       Disk
                    │          │          │
                    └──────────┼──────────┘
                               ▼
                    ┌─────────────────────┐
                    │  Threshold Check    │
                    │       > 85%         │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
             Health Report          Alert Payload
                                         │
                                         ▼
                                  HTTP Webhook
                                         │
                                         ▼
                                  Discord / Slack
```

## DevSecOps Pipeline

```text
Developer
    │
    ▼
Git Commit
    │
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ├── Install dependencies
    │
    ├── Run pytest
    │
    ├── Build Docker image
    │
    └── Trivy security scan
```

## Testing

The project contains automated tests covering monitoring, alerts, and integration.

Current local test result:

```text
8 passed
```

Run tests locally:

```bash
pytest
```

## Docker

Build the Docker image:

```bash
docker build -t server-health-monitor .
```

Run the container:

```bash
docker run --rm server-health-monitor
```

## CI/CD

GitHub Actions automatically runs the following pipeline on pushes and pull requests to `main`:

1. Checkout repository
2. Set up Python
3. Install dependencies
4. Run pytest
5. Build Docker image
6. Scan Docker image with Trivy

Pipeline:

```text
Code
  │
  ▼
Automated Tests
  │
  ▼
Docker Build
  │
  ▼
Security Scan
  │
  ▼
CI Result
```

## Security

The project uses Trivy to scan the Docker image for known vulnerabilities.

The security scan is configured to detect:

- HIGH vulnerabilities
- CRITICAL vulnerabilities

Security scanning is integrated directly into the CI pipeline.

## Project Structure

```text
automated-server-health-monitor/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   └── monitor.py
│
├── tests/
│   ├── test_alerts.py
│   ├── test_integration.py
│   └── test_monitor.py
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Current Capabilities

The application currently:

- Monitors CPU usage
- Monitors memory usage
- Monitors disk usage
- Applies an 85% threshold
- Generates a JSON health report
- Supports HTTP webhook notifications
- Runs inside a Docker container
- Has automated pytest tests
- Uses GitHub Actions for CI
- Builds the Docker image in CI
- Performs container security scanning with Trivy

## Learning Outcomes

This project demonstrates practical experience with:

- Python automation
- Linux system monitoring
- REST/webhook integration
- Automated testing
- Docker containerization
- Git and GitHub
- GitHub Actions
- CI/CD pipelines
- Container security scanning
- DevSecOps practices

## Future Improvements

Planned improvements include:

- Docker image optimization
- Vulnerability remediation
- Container registry integration
- Infrastructure as Code
- Cloud deployment
- Kubernetes deployment
- Monitoring dashboards
- Centralized logging
- Additional security controls

## Author

**Srinivas Aluri**

This project is part of my transition from infrastructure and engineering into DevSecOps, Cloud, and Cloud Security.