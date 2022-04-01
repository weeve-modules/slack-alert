"""
All constants specific to the application
"""
from app.utils.env import env
from app.utils.floatenv import floatenv


APPLICATION = {
    "INPUT_LABEL": env("INPUT_LABEL", "temperature"),
    "INPUT_UNIT": env("INPUT_UNIT", "Celsius"),
    "ALERT_SEVERITY": env("ALERT_SEVERITY", "warning"),
    "ALERT_MESSAGE": env("ALERT_MESSAGE", "The Reading Shows"),
    "SLACK_WEBHOOK_URL": env("SLACK_WEBHOOK_URL", "xxx")
}
