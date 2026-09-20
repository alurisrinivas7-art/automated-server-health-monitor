# Automated Server Health Monitor

A Python-based Linux server monitoring tool that checks CPU, memory, and disk usage and sends alerts when resource utilization exceeds a defined threshold.

## Project Status

Phase 1 — Initial development

## Objectives

- Monitor Linux server health
- Collect CPU, memory, and disk usage
- Detect resource usage above 85%
- Generate structured JSON alert payloads
- Send notifications through an HTTP webhook
- Practice Python automation and Linux system administration

## Technology Stack

- Python
- Linux / Ubuntu
- Git & GitHub
- HTTP / REST
- JSON
- Discord or Slack Webhooks
- pytest

## Planned Architecture

```text
Linux Server
     |
     v
Python Health Monitor
     |
     +---- CPU
     +---- Memory
     +---- Disk
     |
     v
Threshold Check
     |
     v
JSON Alert
     |
     v
HTTP Webhook
     |
     v
Discord / Slack