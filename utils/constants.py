import configparser
import os

#read config file
config = configparser.ConfigParser()
config.read('/Workspace/Repos/mushroomred933@gmail.com/ecommerce-data-platform/config/config.conf')

#AWS settings

AWS_ACCESS_KEY_ID = config.get('aws','aws_access_key')
AWS_SECRET_ACCESS_KEY = config.get('aws','aws_secret_key')
BUCKET = config.get('aws','aws_bucket_name')
REGION = config.get('aws','aws_region')

