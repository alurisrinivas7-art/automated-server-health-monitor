import json
import psutil

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


if __name__ == "__main__":
    main()