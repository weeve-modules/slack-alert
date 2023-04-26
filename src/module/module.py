"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
import json
import requests
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

    try:
        message = received_data[PARAMS["MESSAGE_LABEL"]]
        slack_data = json.dumps({"text": message})

        log.debug(f"Slack data: {slack_data}")

        response = requests.post(
            url=PARAMS["SLACK_WEBHOOK_URL"],
            data=slack_data,
            headers={"Content-Type": "application/json"},
        )

        # Error handling
        if response.status_code != 200:
            raise ValueError(
                "Request to slack returned an error %s, the response is:\n%s"
                % (response.status_code, response.text)
            )

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
