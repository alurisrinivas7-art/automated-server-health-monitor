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

def send_warnings(webhook_url, warnings):
    """Send all warning messages as a single webhook alert."""

    if not warnings:
        return None

    message = "\n".join(warnings)

    return send_webhook(webhook_url, message)
