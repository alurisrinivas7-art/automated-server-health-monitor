from src.monitor import check_threshold
from src.monitor import get_warning_messages


def test_below_threshold():
    assert check_threshold(84.9) == "OK"


def test_at_threshold():
    assert check_threshold(85.0) == "OK"


def test_above_threshold():
    assert check_threshold(85.1) == "WARNING"

def test_no_warning_messages():
    report = {
        "threshold": 85.0,
        "status": {
            "cpu": "OK",
            "memory": "OK",
            "disk": "OK",
        },
        "metrics": {
            "cpu_percent": 20.0,
            "memory_percent": 40.0,
            "disk_percent": 50.0,
        },
    }

    assert get_warning_messages(report) == []


def test_warning_messages():
    report = {
        "threshold": 85.0,
        "status": {
            "cpu": "WARNING",
            "memory": "OK",
            "disk": "WARNING",
        },
        "metrics": {
            "cpu_percent": 92.0,
            "memory_percent": 40.0,
            "disk_percent": 91.0,
        },
    }

    warnings = get_warning_messages(report)

    assert warnings == [
        "CPU usage is high: 92.0%",
        "DISK usage is high: 91.0%",
    ]