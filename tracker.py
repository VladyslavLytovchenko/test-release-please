import json
import boto3

def lambda_handler(event, context):
    secretsmanager_client = boto3.client('secretsmanager', region_name=event['region'])
    cloudwatch_client = boto3.client('cloudwatch', region_name='us-west-2')

    secret_name = event['secret_name2']

    return {
        'statusCode': 200,
    }
