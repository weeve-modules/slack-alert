"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
import socket
import json
import requests
import time
from .params import PARAMS

log = getLogger("module")


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    now = time.localtime()
    current_time = time.strftime("%H:%M:%S", now)

    try:
        parsed_data = received_data[PARAMS['INPUT_LABEL']]
        device_name = socket.gethostname()

        # This is a way to format the data in a way that Slack can understand.
        replacement_dict = {
            '{{time}}': str(current_time),
            '{{value}}':  str(parsed_data),
            '{{label}}':  PARAMS['INPUT_LABEL'],
            '{{unit}}': PARAMS['INPUT_UNIT'],
            '{{device_name}}': str(device_name),
            '{{alert_severity}}': PARAMS['ALERT_SEVERITY'],
        }

        alert_message = PARAMS['ALERT_MESSAGE']
        for key, value in replacement_dict.items():
            alert_message = alert_message.replace(key, value)

        slack_data = json.dumps({'text': alert_message})

        log.debug(f"Slack data: {slack_data}")
        log.debug(f"Replacement dict: {replacement_dict}")

        response = requests.post(url=PARAMS['SLACK_WEBHOOK_URL'], data=slack_data, headers={
            'Content-Type': 'application/json'})

        # Error handling
        if response.status_code != 200:
            raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (
                response.status_code, response.text))

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
