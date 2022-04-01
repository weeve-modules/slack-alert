"""
All logic related to the module's main application
Mostly only this file requires changes
"""

import socket
import json
import requests
import time

from app.config import APPLICATION


# Set module settings
__INPUT_LABEL__ = APPLICATION['INPUT_LABEL']
__INPUT_UNIT__ = APPLICATION['INPUT_UNIT']
__ALERT_SEVERITY__ = APPLICATION['ALERT_SEVERITY']
__ALERT_MESSAGE__ = APPLICATION['ALERT_MESSAGE']
__SLACK_WEBHOOK_URL__ = APPLICATION['SLACK_WEBHOOK_URL']


def module_main(data):
    """
    Implement module logic here. Although this function returns data, remember to implement
    egressing method to external database or another API.

    Args:
        data ([JSON Object]): [Data received by the module and validated by data_validation function]

    Returns:
        [string, string]: [data, error]
    """

    now = time.localtime()
    current_time = time.strftime("%H:%M:%S", now)
    print(current_time)

    try:
        parsed_data = data[__INPUT_LABEL__]
        device_name = socket.gethostname()

       # This is a way to format the data in a way that Slack can understand.
        replacement_dict = {
            '{{time}}': str(current_time),
            '{{value}}':  str(parsed_data),
            '{{label}}':  __INPUT_LABEL__,
            '{{unit}}': __INPUT_UNIT__,
            '{{device_name}}': str(device_name),
            '{{alert_severity}}': __ALERT_SEVERITY__,
        }

        alert_message = __ALERT_MESSAGE__
        for key, value in replacement_dict.items():
            alert_message = alert_message.replace(key, value)

        slack_data = json.dumps({'text': alert_message})

        print("---------------------------------")
        print(slack_data)
        print(replacement_dict)
        print("---------------------------------")

        response = requests.post(url=__SLACK_WEBHOOK_URL__, data=slack_data, headers={
            'Content-Type': 'application/json'})

        # Error handling
        if response.status_code != 200:
            raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (
                response.status_code, response.text))

        return parsed_data, None
    except Exception:
        return None, "Unable to perform the module logic"
