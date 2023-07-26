import sys
import boto3

ec2_client = boto3.client('ec2', region_name="us-east-1")

def apply_tags_to_ec2(ec2_instance_id, tags):
    try:
        instance = ec2_client.describe_instances(InstanceIds=[ec2_instance_id])
        existing_tags = {tag['Key']: tag['Value'] for tag in instance['Reservations'][0]['Instances'][0]['Tags']}
        existing_tags.update(tags)
        ec2_client.create_tags(Resources=[ec2_instance_id], Tags=[{'Key': k, 'Value': v} for k, v in existing_tags.items()])
        return True
    
    except Exception as e:
        print(f"Error applying tags to EC2 instance {ec2_instance_id}: {e}")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python aws_tagging_script.py <ec2_instance_id> <tag1_key:tag1_value> <tag2_key:tag2_value> ...")
        sys.exit(1)

    ec2_instance_id = sys.argv[1]

    tags_to_apply = {k: v for tag in sys.argv[2:] for k, v in [tag.split(':')]}

    service_completed = apply_tags_to_ec2(ec2_instance_id, tags_to_apply)

    if service_completed:
        print("Tags were successfully applied to the EC2 instance.")
    else:
        print("Failed to apply tags to EC2 instance.")

if __name__ == "__main__":
    main()
