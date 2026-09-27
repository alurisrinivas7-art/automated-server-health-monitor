import os


def get_webhook_url():
    """Read the webhook URL from an environment variable."""

    return os.getenv("WEBHOOK_URL")