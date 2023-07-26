import os
import sys
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient

def authenticate_azure():

    # Retrieve credentials from the environment using ServicePrincipalCredentials

    client_id = os.environ.get("AZURE_CLIENT_ID")
    client_secret = os.environ.get("AZURE_CLIENT_SECRET")
    tenant_id = os.environ.get("AZURE_TENANT_ID")
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")

    credentials = ServicePrincipalCredentials(
        client_id=client_id,
        secret=client_secret,
        tenant=tenant_id
    )

    return ComputeManagementClient(credentials, subscription_id)

compute_client = authenticate_azure()

def apply_tags_to_vm(resource_group_name, vm_name, tags):
    try:
        vm = compute_client.virtual_machines.get(resource_group_name, vm_name)
        existing_tags = vm.tags or {}  # If no tags exist, set existing_tags to an empty dictionary
        existing_tags.update(tags)
        vm.tags = existing_tags
        compute_client.virtual_machines.create_or_update(resource_group_name, vm_name, vm)
        return True
    except Exception as e:
        print(f"Error applying tags to VM {vm_name}: {e}")
        return False


def main():
    if len(sys.argv) < 4:
        print("Usage: python azure_tagging_script.py <resource_group_name> <vm_name> <tag1_key:tag1_value> <tag2_key:tag2_value> ...")
        sys.exit(1)

    resource_group_name = sys.argv[1]
    vm_id = sys.argv[2]
    tags_to_apply = {k: v for tag in sys.argv[3:] for k, v in [tag.split(':')]}

    service_completed = apply_tags_to_vm(resource_group_name, vm_id, tags_to_apply)
    
    if service_completed:
        print("Tags were successfully applied to the VM.")
    else:
        print("Failed to apply tags to the VM.")

if __name__ == "__main__":
    main()
