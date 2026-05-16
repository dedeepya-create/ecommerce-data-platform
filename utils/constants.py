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
print (AWS_ACCESS_KEY_ID )
print (AWS_SECRET_ACCESS_KEY)
#path settings

INPUT_PATH = config.get('file_path','input_path')
GOLD = config.get('gold_path','gold')
SILVER = config.get('silver_path','silver')
BRONZE = config.get('bronze_path','bronze')

#file name settings


ORDERS = config.get('file_names','orders')
PAYMENTS = config.get('file_names','payments')
PRODUCTS = config.get('file_names','products')
CUSTOMERS = config.get('file_names','customers')


