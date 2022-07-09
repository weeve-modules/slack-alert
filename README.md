# Slack Alert

|              |                                                                                |
| ------------ | ------------------------------------------------------------------------------ |
| name         | Slack Alert                                                                    |
| version      | v1.0.0                                                                         |
| GitHub       | [weeve-modules/slack-alert](https://github.com/weeve-modules/slack-alert)                    |
| DockerHub    | [weevenetwork/slack-alert](https://hub.docker.com/r/weevenetwork/slack-alert)  |
| authors      | Jakub Grzelak, Paul Gaiduk                                                     |

***
## Table of Content

- [Slack Alert](#slack-alert)
  - [Table of Content](#table-of-content)
  - [Description](#description)
  - [Sample Notifications](#sample-notifications)
  - [Module Variables](#module-variables)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
***

## Description

Slack Alert is an alerting module responsible for sending notifications to Slack channels when triggered.
This module is containerized using Docker.

## Sample Notifications

| Type        | Text                  |
| ----------- | --------------------- |
| warning     | _WARNING for MachineName! Temperature reading shows 41.19 Celsius._               |
| alarming    | _ALARM from MachineName! Detected an alarming reading of Temperature: 100 Celsius._ |
| caution     | _CAUTION for MachineName! Temperature is 100 Celsius._                             |
| broken      | _BROKEN device MachineName! Detected Temperature reading is -1.1 Celsius._         |

## Module Variables

The following module configurations can be provided in a data service designer section on weeve platform:

| Environment Variables | type   | Description                                       |
| --------------------- | ------ | ------------------------------------------------- |
| INPUT_LABEL           | string  | The field to apply alert on, i.e: "temperature"        |
| INPUT_UNIT            | string  | I.e: "Celsius"                                         |
| ALERT_SEVERITY        | string  | Alert type: warning, alarming, caution, broken         |
| ALERT_MESSAGE         | string  | Use string interpolation format to get required field in the alert message -> {{label}}, {{value}}, {{unit}}, {{alert_severity}}, {{device_name}} and {{time}} |
| SLACK_WEBHOOK_URL     | string  | Webhook to the slack channel to put alerts on, format: 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'         |
| MODULE_NAME           | string | Name of the module                                |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)    |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |
| INGRESS_HOST          | string | Host to which data will be received               |
| INGRESS_PORT          | string | Port to which data will be received               |

## Dependencies

The following are module dependencies:

* bottle
* requests

## Input

Input to this module is JSON body single object:

Example:
```json
{
  temperature: 15
}
```

## Output

This module does not produce any output except Slack notifications.
