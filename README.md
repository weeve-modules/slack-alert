# Slack Alert

|           |                                                                               |
| --------- | ----------------------------------------------------------------------------- |
| name      | Slack Alert                                                                   |
| version   | v2.0.0                                                                        |
| GitHub    | [weeve-modules/slack-alert](https://github.com/weeve-modules/slack-alert)     |
| DockerHub | [weevenetwork/slack-alert](https://hub.docker.com/r/weevenetwork/slack-alert) |
| authors   | Jakub Grzelak, Paul Gaiduk                                                    |

***
## Table of Content

- [Slack Alert](#slack-alert)
  - [Table of Content](#table-of-content)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
***

## Description

Slack Alert is an alerting module responsible for sending notifications to Slack channels when triggered. It works best with messages provided by the [Message Composer](https://github.com/weeve-modules/message-composer) module.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Environment Variables | type   | Description                                                                                                                            |
| --------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| MESSAGE_LABEL         | string | JSON label which contains the message text (as created by message composer module)                                                     |
| SLACK_WEBHOOK_URL     | string | Webhook to the slack channel to put alerts on, format: 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX' |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                                                                          |
| --------------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| MODULE_NAME           | string | Name of the module                                                                                   |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)                                                       |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |
| INGRESS_HOST          | string | Host to which data will be received                                                                  |
| INGRESS_PORT          | string | Port to which data will be received                                                                  |

## Dependencies

The following are module dependencies:

* bottle
* requests

## Input

Input to this module is JSON body single object:

Example:
```json
{
  "message": "Measured temperature at node Floor 1 South reached 25 Celsius"
}
```

## Output

This module does not produce any output except Slack notifications.
