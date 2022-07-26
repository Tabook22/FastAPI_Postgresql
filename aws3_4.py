#source:https://hands-on.cloud/working-with-s3-in-python-using-boto3/#:~:text=To%20create%20the%20Amazon%20S3,all%20AWS%20accounts%20and%20customers.
#creating new bucket using boto3 client
#-----------------------------------------
''''
import boto3

AWS_REGION = "us-east-2"
client = boto3.client("s3", region_name=AWS_REGION)
bucket_name = "allmona2"
location = {'LocationConstraint': AWS_REGION}
response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")
'''



#creating new bucket using boto3 resource
#-----------------------------------------
'''
import boto3

AWS_REGION = "us-west-1"

resource = boto3.resource("s3", region_name=AWS_REGION)

bucket_name = "allmona1"
location = {'LocationConstraint': AWS_REGION}

bucket = resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")
'''