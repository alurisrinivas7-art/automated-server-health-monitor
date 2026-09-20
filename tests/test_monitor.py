from src.monitor import check_threshold, create_health_report


def test_below_threshold():
    assert check_threshold(84.9) == "OK"


def test_at_threshold():
    assert check_threshold(85.0) == "OK"


def test_above_threshold():
    assert check_threshold(85.1) == "WARNING"


def test_health_report():
    health = {
        "cpu_percent": 20.0,
        "memory_percent": 40.0,
        "disk_percent": 60.0,
    }

    report = create_health_report(health)

    assert report["threshold"] == 85.0
    assert report["status"]["cpu"] == "OK"
    assert report["status"]["memory"] == "OK"
    assert report["status"]["disk"] == "OK"
    assert report["metrics"]["cpu_percent"] == 20.0


def test_health_report_warning():
    health = {
        "cpu_percent": 90.0,
        "memory_percent": 40.0,
        "disk_percent": 95.0,
    }

    report = create_health_report(health)

    assert report["status"]["cpu"] == "WARNING"
    assert report["status"]["memory"] == "OK"
    assert report["status"]["disk"] == "WARNING"