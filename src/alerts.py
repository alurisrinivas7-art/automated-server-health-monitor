import requests


def send_webhook(webhook_url, message):
    """Send a message to an HTTP webhook."""

    payload = {
        "content": message
    }

    response = requests.post(
        webhook_url,
        json=payload,
        timeout=10,
    )

    response.raise_for_status()

    return response.status_code