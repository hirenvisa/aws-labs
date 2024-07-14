import boto3
import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    tableName = "labs_dynamodb_table"

    try:
        # Scan the DynamoDB table
        response = dynamodb.scan(
            TableName=tableName
        )

    # Get the items from the response
        items = response['Items']

    # Create a file to write the data
   
        # Create an array to store the data
        data = []
    
        # Iterate over the items and add them to the array
        for item in items:
            item_list = {}
            allKeys = item.keys()
            for k in allKeys:
                value = list(item[k].values())[0]
                item_list[k] = str(value)
            data.append(item_list)
            data = json.dumps(data)

        # Create an S3 client
        s3 = boto3.client('s3', region_name='us-east-1')

        # Upload the file to the S3 bucket
        s3Response = s3.object("bucket2222222222222", 'data.txt').put(Body=data)
        print("Completed upload to s3.")

        return{
            'statusCode': 200,
            'body': json.dumps("success")
        }

    except ClientError as e:
        print(f"Client error: {str(e)}")
        return{
            'statusCode': 500,
            'body': json.dumps("error")
        }
    except Exception as e:
        print(f"Client error: {str(e)}")
        return{
            'statusCode': 500,
            'body': json.dumps("error")
        }

