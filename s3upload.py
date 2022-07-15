import boto3
from pprint import pprint
import pathlib
import os
s3 = boto3.client("s3", aws_access_key_id='AKIATL5UWEGQ7KUZBHGI', aws_secret_access_key='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')
#def upload_file_using_client():
"""
    Uploads file to S3 bucket using S3 client object
    :return: None
"""
s3 = boto3.client("s3")
bucket_name = "allmona"
object_name = "sample1.txt"
file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), "requirements.txt")
response = s3.upload_file(file_name, bucket_name, object_name)
pprint(response)  # prints None