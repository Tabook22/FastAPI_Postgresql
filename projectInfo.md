
<!-- -----------------------------------------------------------------
information about aws3_3.py
----------------------------------------------------------------->
<h2>aws3_3.py</h2>
<br/>
<a href="https://www.youtube.com/watch?v=Wxe7sdFW8J0">Youtube Good Resource </a>

```python
import boto3
```

<p>
Boto3 is the python SDK to connect to Amazon Web Services(AWS). It allowys you to connect to AWS resoruce, create, delete, update and modify those resoruce.Boto3 is maintained and published by Amazon Web Services.<br/>
Boto (pronounced boh-toh) was named after the fresh water dolphin native to the Amazon river. The name was chosen by the author of the original Boto library, Mitch Garnaat, as a reference to the company.
<br/>
To use boto3 we need to create a client or resources
 </p>
 <p>
 Boto3 usees two different ways to making AWS service requests</p>
 <ul>
 <li>
 Client
 </li>
  <li>
 Resource
 </li>
 </ul>
<h3>First we are starting with client.</h3>

```python
cl=boto3.client("s3")
```
<p>
here we created the client "cl" then we specify the service "s3"
the boto3 knows how to connect to:<br> 
1- The user account<br/>
2- The region 
<br/>
<br/>
because it uses the <b><i>AWS configuraiton file</i></b> which contains all these information, 
the configuraiton file created when we first configure AWS through the AWS CLI
To check the aws configuration we first open the <b><i>.aws</i></b> folder then check the credential file</p>
<br/>
<pre>
(base) nassertabook@Nassers-MacBook-Pro ~ % cd ~/.aws
(base) nassertabook@Nassers-MacBook-Pro .aws % ls
config		credentials
(base) nassertabook@Nassers-MacBook-Pro .aws % cat credentials
[default]
aws_access_key_id = AKIATL5UWEGQ7KUZBHGI
aws_secret_access_key = 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
(base) nassertabook@Nassers-MacBook-Pro .aws % 
</pre>
<br/>
<p>
the boto3 uses the configuraitons inside the creddentials file to connent to our AWS account
the configuraiton file created once we have installed and configured our AWS CLT
for more information go to : https://aws.amazon.com/cli/?nc1=h_ls and follow the steps
</p>

<p>
<br/>
<h3>Using the resources</h3>
boto3.resource is a high-level services class wrap around boto3.client.
boto3.client are low level, you don't have an "entry-class object", thus you  must explicitly specify the exact resources it connects to for every. 
</p>
<p>Resources are the recommended pattern to use boto3 as you don’t have to worry about a lot of the underlying details when interacting with AWS services. As a result, code written with Resources tends to be simpler.</p>
<br/>

```python
#Here s3 bucket identifier
s3 = boto3.resource("s3") # here we creating the resource instance
mybct = s3.Bucket('mybucket')
```
<p>
now mybct object is attaching the S3 bucket name "mybucket" 
</p>

```python
print(mybucket)
```
<br/>
<br/>
<hr>

<h2>aws3_4.py</h2>
<br/>

```python
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
response = client.list_buckets()
for bucket in response['Buckets']:
    print(f'--{bucket['Name]})

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

iterator = resource.buckets.all()
print("Listing Amazon S3 Buckets:")

for bucket in iterator:
    print(f"-- {bucket.name}")
'''
```
<hr>
The new created buckets will be added
<br/>
<img src="img/createbucket.png">
<br/>
<br/>
