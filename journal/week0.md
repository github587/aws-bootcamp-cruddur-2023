# Week 0 — Billing and Architecture

## REQUIRED HOMEWORK

### Install  and verify AWS CLI
Added task to download and install aws cli to gitpod.yml file.
Verified that aws is installed as the workspace opens each time on gitpod by running either aws --version or aws sts get-caller-identity.
Setup user credentials and exported them as gitpod env variables.

![Installing AWS CLI](assets/week0_install_aws_cli_proof.png)

### Created AWS Budget by using budget.json
verified that budget - Example Tag Budget is created on the console for the user.
![Budget alarm json](assets/budget_json_proof1.png)

Screen from console after the AWS create budget command is run.
![Budget console proof](assets/budget_proof_1.png)

### Created billing alarm using AWS CLI on gitpod

First, created SNS topic for the billing alarm using budget-notification.json and verified using the console

![SNS topic json](assets/budget_notication_json_proof1.png)

verified that the SNS topic got created on the AWS admin console

![SNS topic AWS console](assets/billing_alarm_proof.png)

Then, created the billing alarm using alarm-config.jsonn and verified using the console.

![Billing alarm json](assets/alarm_config_proof1.png)

Verified on the AWS adminconsole that the cloud watch alarm is created.

![Daily Estimated Charges CW Alarm](assets/cloudwatch_alarm_proof1.png.png)
### Conceptual diagram /napkin diagram


## HOMEWORK CHALLENGES





