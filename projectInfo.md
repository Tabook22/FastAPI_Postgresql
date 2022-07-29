

# Uing Boto3
## aws3_3.py
### [Good Youtube Resource](https://www.youtube.com/watch?v=Wxe7sdFW8J0")
### Start using boto3 
- What is is boto3?
    - Boto3 is the python SDK to connect to Amazon Web Services(AWS). 
        It allowys you to connect to AWS resoruce, create, delete, update and modify those resoruce.
        Boto3 is maintained and published by Amazon Web Services.
        Boto (pronounced boh-toh) was named after the fresh water dolphin native to the Amazon river. 
        The name was chosen by the author of the original Boto library, Mitch Garnaat, as a reference to the company.
    

- Making AWS service requests
    - Client
        - ```python
            cl=boto3.client("s3")
            '''
            here we created the client "cl" then we specify the service "s3"
            the boto3 knows how to connect to:
            - The user account
            - The region

            because it uses the AWS configuraiton file which contains all these information,
            the configuraiton file created when we first configure AWS through the AWS CLI
            To check the aws configuration we first open the folder then check the credential file


            (base) nassertabook@Nassers-MacBook-Pro ~ % cd ~/.aws
            (base) nassertabook@Nassers-MacBook-Pro .aws % ls
            config credentials
            (base) nassertabook@Nassers-MacBook-Pro .aws % cat credentials

            [default]
            aws_access_key_id = AKIATL5UWEGQ7KUZBHGI
            aws_secret_access_key = 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
            (base) nassertabook@Nassers-MacBook-Pro .aws %

            the boto3 uses the configuraitons inside the creddentials file to connent to our AWS account

            the configuraiton file created once we have installed and configured our AWS CLT
            for more information go to : https://aws.amazon.com/cli/?nc1=h_ls and follow the steps
            '''
            ```
    - Resource
        - ```python
            '''
            boto3.resource is a high-level services class wrap around boto3.client.
            boto3.client are low level, you don't have an "entry-class object", thus you must explicitly specify the exact resources it connects to for every.
            Resources are the recommended pattern to use boto3 as you don’t have to worry about a lot of the underlying details when interacting with AWS services. As a result, code written with Resources tends to be simpler.
            '''
            #Here s3 bucket identifier
            s3 = boto3.resource("s3") # here we creating the resource instance
            mybct = s3.Bucket('mybucket')
            '''
            now mybct object is attaching the S3 bucket name "mybucket"
            '''
            print(mybucket)
            ```

## aws3_4.py
- creating new bucket using boto3 client method
    - ```python
        #source:https://hands-on.cloud/working-with-s3-in-python-using-boto3/#:~:text=To%20create%20the%20Amazon%20S3,all%20AWS%20accounts%20and%20customers.

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
- creating new bucket using boto3 resource method
    - ``` python
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

        ```
- The new created buckets will be added
![](img/createbucket.png)

