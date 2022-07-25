import os
import json
import boto3

def lambda_handler(event, context):
    s3_client = boto3.client('s3') 
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    key = urllib.parse.unquote_plus(key, encoding='utf-8')
                        
    message = 'The file ' + key + ' was uploaded to this bucket ' + bucket_name
    print(message)
