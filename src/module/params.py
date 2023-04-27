"""
All constants specific to the application
"""
from os import getenv


PARAMS = {
    "MESSAGE_LABEL": getenv("MESSAGE_LABEL", "message"),
    "SLACK_WEBHOOK_URL": getenv("SLACK_WEBHOOK_URL"),
}

if PARAMS["SLACK_WEBHOOK_URL"] is None:
    raise ValueError("SLACK_WEBHOOK_URL is not set in the environment variables!")
