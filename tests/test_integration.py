from unittest.mock import patch

from src.monitor import create_health_report, get_warning_messages
from src.alerts import send_warnings


@patch("src.alerts.send_webhook")
def test_warning_alert_integration(mock_send_webhook):
    health = {
        "cpu_percent": 92.0,
        "memory_percent": 40.0,
        "disk_percent": 91.0,
    }

    report = create_health_report(health)
    warnings = get_warning_messages(report)

    mock_send_webhook.return_value = 204

    result = send_warnings(
        "https://example.com/webhook",
        warnings,
    )

    assert result == 204

    mock_send_webhook.assert_called_once_with(
        "https://example.com/webhook",
        "CPU usage is high: 92.0%\nDISK usage is high: 91.0%",
    )