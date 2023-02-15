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

### Created billing alarm using AWS CLI on gitpod

First, created SNS topic for the billing alarm using budget-notification.json and verified using the console

![Budget alarm json](assets/budget_notication_json_proof.png)

Then, created the billing alarm using alarm-config.jsonn and verified using the console.

![Budget alarm json](assets/alarm_config_proof.png)

### Conceptual diagram /napkin diagram


## HOMEWORK CHALLENGES





