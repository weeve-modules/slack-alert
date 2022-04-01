"""
All logic related to the module's main application
Mostly only this file requires changes
"""

import socket
import json
import requests

from app.config import APPLICATION


# Set module settings
__INPUT_LABEL__ = APPLICATION['INPUT_LABEL']
__INPUT_UNIT__ = APPLICATION['INPUT_UNIT']
__ALERT_SEVERITY__ = APPLICATION['ALERT_SEVERITY']
__ALERT_MESSAGE__ = APPLICATION['ALERT_MESSAGE']
__SLACK_WEBHOOK_URL__ = APPLICATION['SLACK_WEBHOOK_URL']

slack_message = {
    "warning": f'WARNING for %s! %s %s %s %s',
    "alarming": f'ALARM from %s! %s %s: %s %s',
    "caution": f'CAUTION for %s! %s %s %s %s',
    "broken": f'BROKEN device %s!%s %s %s %s',
}

def module_main(data):
    """
    Implement module logic here. Although this function returns data, remember to implement
    egressing method to external database or another API.

    Args:
        data ([JSON Object]): [Data received by the module and validated by data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        parsed_data = data[__INPUT_LABEL__]
        
        # prepare the slack POST message
        # SLACK DOC: https://api.slack.com/messaging/webhooks
        device_name = socket.gethostname()
        slack_data = json.dumps({'text': slack_message[__ALERT_SEVERITY__] % (device_name,__ALERT_MESSAGE__ ,__INPUT_LABEL__, parsed_data, __INPUT_UNIT__)})

        # POST notification to Slack API
        response = requests.post(url=__SLACK_WEBHOOK_URL__, data=slack_data, headers={'Content-Type': 'application/json'})

        # Error handling
        if response.status_code != 200:
            raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))

        return parsed_data, None
    except Exception:
        return None, "Unable to perform the module logic"