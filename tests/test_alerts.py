from unittest.mock import Mock, patch

from src.alerts import send_webhook


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