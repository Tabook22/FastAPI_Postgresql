#source:https://www.youtube.com/watch?v=Wxe7sdFW8J0

import boto3 
#using client
cl=boto3.client("s3") 

#using Resources
s3 = boto3.resource("s3")
mybucket = s3.Bucket('mybucket')
print(mybucket)