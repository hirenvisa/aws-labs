import boto3
import json
import time
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Create EC2 client
    ec2_client = boto3.client('ec2')

    try:
        # Specify the parameters for the new EC2 instance
        instance_params = {
            'ImageId': 'ami-0b69ea66ff7391e80',  # Replace with the desired AMI ID
            'InstanceType': 't2.micro',  # Replace with the desired instance type
            'MinCount': 1,
            'MaxCount': 1
        }

        # Create the EC2 instance
        response = ec2_client.run_instances(**instance_params)

        print(response['Instances'][0], "EC2 Instance created.")

        # Print the instance ID of the newly created instance
        instance_id = response['Instances'][0]['InstanceId']
        print(f"New EC2 instance created with ID: {instance_id}")

        return {
            'statusCode': 200,
            'body': json.dumps("success")
        }
    except ClientError as e:
        print("Error creating EC2 instance:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps("error")
        }
    except Exception as e:
        print("Error creating EC2 instance:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps("error")
        }

