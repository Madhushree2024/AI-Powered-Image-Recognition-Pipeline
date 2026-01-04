import boto3
import json
import urllib.parse

# Initialize the AWS clients
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageLabels') # Must match your DynamoDB table name

def lambda_handler(event, context):
    # 1. Get the bucket and file name from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    try:
        # 2. Call AWS Rekognition to detect objects
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=10,
            MinConfidence=80
        )
        
        # 3. Format the labels into a simple list
        labels = [label['Name'] for label in response['Labels']]
        print(f"Detected labels for {key}: {labels}")
        
        # 4. Save the results to DynamoDB
        table.put_item(
            Item={
                'ImageID': key,
                'Labels': labels,
                'RawData': json.dumps(response['Labels'])
            }
        )
        
        return {"status": "success", "labels": labels}
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
