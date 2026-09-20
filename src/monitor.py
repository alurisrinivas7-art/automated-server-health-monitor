import psutil

THRESHOLD = 85.0


def get_system_health():
    """Collect current CPU, memory, and disk usage."""

    cpu = psutil.cpu_percent(interval=1)
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


def main():
    health = get_system_health()

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


if __name__ == "__main__":
    main()