import boto3 # boto3 is python SDK to connect to AWS. It allowys you to connect to AWS resoruce, create, delete, update and modify those resoruce
#to use boto2 we need to create a client or resources
cl=boto3.client("s3") 
#here we created the client "cl" then we specify the service "s3"
#the boto3 athenticate with my AWS account, 
# that happent because when we first configure AWS through the CLI
'''
To check the aws configuration we first open the .aws folder then check the credential file
----------------------------------------------------------------
(base) nassertabook@Nassers-MacBook-Pro ~ % cd ~/.aws
(base) nassertabook@Nassers-MacBook-Pro .aws % ls
config		credentials
(base) nassertabook@Nassers-MacBook-Pro .aws % cat credentials
[default]
aws_access_key_id = AKIATL5UWEGQ7KUZBHGI
aws_secret_access_key = 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
(base) nassertabook@Nassers-MacBook-Pro .aws % 

'''
#the boto3 uses the configuraitons inside the creddentials file to connent to our AWS account
