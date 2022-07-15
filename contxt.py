#This file keeps the settings of our local postgresql server
#This is important, because when we push our files to github we can ignore these data and not pushing them, and keep our data secure
db_settings={    
"t_host" : "localhost",
"t_port" : "5432",
"t_dbname" : "mydb",
"t_name_user" : "Nasser22",
"t_password" : "Goo@allmona_22",
}

s3_settings={
    's3_BUCKET_NAME' :'allmona',
    'access_key':'AKIATL5UWEGQ7KUZBHGI',
    'access_secret':'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',
    'region':'us-west-1'
             }