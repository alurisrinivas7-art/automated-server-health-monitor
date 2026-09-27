import json
import psutil

from src.alerts import send_warnings
from src.config import get_webhook_url

THRESHOLD = 85.0


def get_system_health():
    """Collect current CPU, memory, and disk usage."""

    cpu = max(0.0, psutil.cpu_percent(interval=1))
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    return {
        "cpu_percent": cpu,
        "memory_percent": memory,
        "disk_percent": disk,
    }


def check_threshold(value):
    """Return WARNING when a metric exceeds the threshold."""

    if value > THRESHOLD:
        return "WARNING"

    return "OK"


def create_health_report(health):
    """Create a structured JSON-compatible health report."""

    return {
        "threshold": THRESHOLD,
        "status": {
            "cpu": check_threshold(health["cpu_percent"]),
            "memory": check_threshold(health["memory_percent"]),
            "disk": check_threshold(health["disk_percent"]),
        },
        "metrics": health,
    }

def get_warning_messages(report):
    """Create alert messages for metrics above the threshold."""

    warnings = []

    for metric, status in report["status"].items():
        if status == "WARNING":
            value = report["metrics"][f"{metric}_percent"]
            warnings.append(
                f"{metric.upper()} usage is high: {value}%"
            )

    return warnings

def main():
    health = get_system_health()
    report = create_health_report(health)

    print("Server Health")
    print("-------------")

    print(
        f"CPU Usage:    {health['cpu_percent']}% "
        f"[{check_threshold(health['cpu_percent'])}]"
    )

    print(
        f"Memory Usage: {health['memory_percent']}% "
        f"[{check_threshold(health['memory_percent'])}]"
    )

    print(
        f"Disk Usage:   {health['disk_percent']}% "
        f"[{check_threshold(health['disk_percent'])}]"
    )

    print("\nJSON Health Report")
    print("------------------")
    print(json.dumps(report, indent=2))

    warnings = get_warning_messages(report)

    if warnings:
        print("\nWarnings")
        print("--------")

        for warning in warnings:
            print(f"WARNING: {warning}")


    webhook_url = get_webhook_url()

    if warnings and webhook_url:
        send_warnings(webhook_url, warnings)
        print("\nWebhook alert sent.")


    webhook_url = get_webhook_url()

    if warnings and webhook_url:
        send_warnings(webhook_url, warnings)
        print("\nAlert sent successfully.")


if __name__ == "__main__":
    main()