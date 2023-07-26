# Cloud VM Tagging Service

This project consists of two Python scripts that provide the functionality to apply tags to AWS EC2 instances and Azure virtual machines (VMs). These scripts allow you to add custom tags to your cloud resources, providing better organization and management of your infrastructure.

## AWS Tagging Script

The AWS tagging script (`aws_tagging_script.py`) allows you to apply tags to AWS EC2 instances. The script utilizes the Boto3 library to interact with AWS services.

### Prerequisites

1. Python 3.x installed on your system.
2. Boto3 library for AWS interactions: pip install boto3

### Usage

To use the AWS tagging script, run the following command in your terminal or command prompt: 
(```)python aws_tagging_script.py <ec2_instance_id> <tag1_key:tag1_value> <tag2_key:tag2_value> ...(```)
- `<ec2_instance_id>`: The ID of the EC2 instance to which you want to apply tags.
- `<tag1_key:tag1_value> <tag2_key:tag2_value> ...`: Provide one or more key-value pairs for the tags you want to apply to the EC2 instance.

## Azure Tagging Script

The Azure tagging script (`azure_tagging_script.py`) allows you to apply tags to Azure virtual machines (VMs). The script uses the Azure SDK for Python.

### Prerequisites

1. Python 3.x installed on your system.
2. Azure SDK for Python: pip install azure-common azure-mgmt-compute azure-mgmt-resource

### Usage

To use the Azure tagging script, run the following command in your terminal or command prompt:
(```)python azure_tagging_script.py <resource_group_name> <vm_name> <tag1_key:tag1_value> <tag2_key:tag2_value> ...(```)

- `<resource_group_name>`: The name of the Azure resource group where the VM is located.
- `<vm_name>`: The name of the Azure VM to which you want to apply tags.
- `<tag1_key:tag1_value> <tag2_key:tag2_value> ...`: Provide one or more key-value pairs for the tags you want to apply to the VM.

Note: Ensure that you have the necessary credentials and permissions to interact with AWS and Azure services.



