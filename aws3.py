import io
import boto3

s3=boto3.client("s3")
s3.upload_file("img/myimg.jpeg",'allmona','myimg.jpeg')


'''
# declare things here
bucket = 'your-s3-bucket-name'
path = 'img/myimg.jpeg'

# image
img = 'your image file here'

# set client
client = boto3.client('s3')

# save image file in memory and store in s3
temp_file = io.BytesIO()
img.save(temp_file, format=img.format)
temp_file.seek(0)
client.upload_fileobj(temp_file, bucket, path)
'''