#source:https://www.youtube.com/watch?v=1D9ggTJ9Ejc
import boto3
import requests

OBJECT_NAME_TO_UPLOAD='img/myimg.jpeg'
s3_client=boto3.client(
    's3',
    aws_access_key_id='AKIATL5UWEGQ7KUZBHGI',
    aws_secret_access_key='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'
)

#generate the presigned url
response=s3_client.generate_presigned_post(
    Bucket='allmona',
    Key=OBJECT_NAME_TO_UPLOAD,
    ExpiresIn=10 #How long the website will stay alive in seconds otherwise we will get rejected request
)

#use the values inside the response
print(response)

#Upload file to S3 using presigned url
files={'file': open(OBJECT_NAME_TO_UPLOAD, 'rb')} # rb means read in bytes or binary, that means open the file and read it in bytes or binary

#here rsp represents the second response, the first response will create the presigned url
rsp=requests.post(response['url'],data=response['fields'], files=files)
print(rsp.status_code)