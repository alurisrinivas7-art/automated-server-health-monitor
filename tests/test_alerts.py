from unittest.mock import Mock, patch

from src.alerts import send_webhook, send_warnings


@patch("src.alerts.requests.post")
def test_send_webhook(mock_post):
    mock_response = Mock()
    mock_response.status_code = 204
    mock_post.return_value = mock_response

    result = send_webhook(
        "https://example.com/webhook",
        "Server CPU usage is high",
    )

    assert result == 204

    mock_post.assert_called_once_with(
        "https://example.com/webhook",
        json={"content": "Server CPU usage is high"},
        timeout=10,
    )

    mock_response.raise_for_status.assert_called_once()


@patch("src.alerts.send_webhook")
def test_send_warnings(mock_send_webhook):
    mock_send_webhook.return_value = 204

    warnings = [
        "CPU usage is high: 92.0%",
        "DISK usage is high: 91.0%",
    ]

    result = send_warnings(
        "https://example.com/webhook",
        warnings,
    )

    assert result == 204

    mock_send_webhook.assert_called_once_with(
        "https://example.com/webhook",
        "CPU usage is high: 92.0%\nDISK usage is high: 91.0%",
    )