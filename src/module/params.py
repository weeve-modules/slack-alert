"""
All constants specific to the application
"""
from os import getenv


PARAM = {
    "INPUT_LABEL": getenv("INPUT_LABEL", "temperature"),
    "INPUT_UNIT": getenv("INPUT_UNIT", "Celsius"),
    "ALERT_SEVERITY": getenv("ALERT_SEVERITY", "warning"),
    "ALERT_MESSAGE": getenv("ALERT_MESSAGE", "Data point {{label}} reached the value of {{value}} {{unit}} at {{time}}"),
    "SLACK_WEBHOOK_URL": getenv("SLACK_WEBHOOK_URL", "xxx")
}
