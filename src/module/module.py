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
from params import PARAM

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
    print(current_time)

    try:
        parsed_data = received_data[PARAM['INPUT_LABEL']]
        device_name = socket.gethostname()

       # This is a way to format the data in a way that Slack can understand.
        replacement_dict = {
            '{{time}}': str(current_time),
            '{{value}}':  str(parsed_data),
            '{{label}}':  PARAM['INPUT_LABEL'],
            '{{unit}}': PARAM['INPUT_UNIT'],
            '{{device_name}}': str(device_name),
            '{{alert_severity}}': PARAM['ALERT_SEVERITY'],
        }

        alert_message = PARAM['ALERT_MESSAGE']
        for key, value in replacement_dict.items():
            alert_message = alert_message.replace(key, value)

        slack_data = json.dumps({'text': alert_message})

        print("---------------------------------")
        print(slack_data)
        print(replacement_dict)
        print("---------------------------------")

        response = requests.post(url=PARAM['SLACK_WEBHOOK_URL'], data=slack_data, headers={
            'Content-Type': 'application/json'})

        # Error handling
        if response.status_code != 200:
            raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (
                response.status_code, response.text))

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
