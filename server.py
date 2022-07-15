from contxt import db_settings as dbst 
from dotenv import load_dotenv   #for python-dotenv method
import os 
import boto3
import uvicorn
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import List
import psycopg2
from fastapi import FastAPI , UploadFile

#for python-dotenv method, the .env is the root folder if it is in different folder use "load_dotenv(path/to/.evn"
load_dotenv()  

''' 
s3_BUCKET_NAME ="allmona"
access_key='AKIATL5UWEGQ7KUZBHGI'
access_secret='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'
region="us-west-1"
'''


class usrevents_img (BaseModel):
    imgid:int 
    img_title:str 
    img_url:str
    img_desc:str 
    evt_id:int 
    created_at:datetime
    updated_dat:datetime 
    last_login:datetime
    is_deleted:bool
    

app=FastAPI(debug=True)

@app.get('/status')
async def check_status():
    return "In The name of Allah"

@app.get("/photos", response_model=List[usrevents_img])
async def get_all_photos():
    #connection to database
    #db_conn = psycopg2.connect(host="localhost", port="5432", dbname="mydb", user="Nasser22", password="Allmona_22")
    db_conn = psycopg2.connect(
         host=os.environ.get('PG_HOST'),
         port=os.environ.get('PG_PORT'),
         dbname=os.environ.get('PG_DBNAME'),
         user=os.environ.get('PG_USER'),
         password=os.environ.get('PG_PASSWORD'))
    
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT * FROM usrevents_img ORDER BY imgid DESC ")
    rows=db_cursor.fetchall()
    formatted_photos=[]
    for row in rows:
        formatted_photos.append(
           usrevents_img(imgid=row[0],img_title=row[1],img_url=row[2],img_desc=row[3],evt_id=row[4],created_at=row[5],updated_dat=row[6],last_login=row[7],is_deleted=row[8])
            ) 
    
    #do some clean up
    db_cursor.close()
    db_conn.close()

    #return all the photos
    return formatted_photos


@app.post("/photos", status_code=201)
async def add_photos(file: UploadFile):
    print("In The Name of God")
    print(file.filename)
    print(file.content_type)
    #upload our file to AWS S3
    '''
    s3=boto3.client("s3",aws_access_key_id=access_key, aws_secret_access_key=access_secret)
    try:
        s3.upload_file(
            file.file,format,
            s3_BUCKET_NAME,
            file.filename
        )
    except Exception as e:
        print(e)

    '''
    
  
    s3=boto3.resource("s3",
                      aws_access_key_id=os.environ.get('ACCESS_KEY'),
                      aws_secret_access_key=os.environ.get('ACCESS_SECRET'),
                      region_name=os.environ.get('REGION'),)
    bucket=s3.Bucket(os.environ.get('s3_BUCKET_NAME'))
    
    #once we have our resource to the bucket we are going to upload our file
    bucket.upload_fileobj(file.file, file.filename, ExtraArgs={"ACL":"public-read"})
    
    #now this should our url
    uploaded_file_url=f"https://{os.environ.get('s3_BUCKET_NAME')}.s3.amazonaws.com/{file.filename}"
    file_desc="In The Name of Allah"  
    

    
    #now we know the url we are going to store our url in the database
    db_conn = psycopg2.connect(host="localhost", port="5432", dbname="mydb", user="Nasser22", password="Allmona_22")
    db_cursor = db_conn.cursor()
    db_cursor.execute(f"INSERT INTO usrevents_img (img_title,img_url, img_desc, evt_id) VALUES('{file.filename}','{uploaded_file_url}','{file_desc}',1)")

    #now the data is inserted we need to commit our data insertion
    db_conn.commit()
    
        #do some clean up
    db_cursor.close()
    db_conn.close()
    
    
    
if __name__ == "__main__":
    # host="0.0.0.0" tells a server to "listen" for and accept connections from any IP address. On PCs and client devices. A 0.0. 0.0 address indicates the client isn't connected to a TCP/IP network,
    uvicorn.run(app, host="0.0.0.0", reload=False)
    