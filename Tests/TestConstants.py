import sys
sys.path.insert(0,'/Workspace/Repos/mushroomred933@gmail.com/ecommerce-data-platform/')

from utils.constants import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    BUCKET,
    REGION,
    INPUT_PATH,
    GOLD,
    SILVER,
    BRONZE,
    CUSTOMERS,
    ORDERS,
    PRODUCTS,
    PAYMENTS
)

print (f"AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID}")
print (f"AWS_SECRET_ACCESS_KEY: {AWS_SECRET_ACCESS_KEY}")
print (f"BUCKET: {BUCKET}")
print (f"REGION: {REGION}")
print (f"INPUT_PATH: {INPUT_PATH}")
print (f"GOLD: {GOLD}")
print (f"SILVER: {SILVER}")
print (f"BRONZE: {BRONZE}")
print (f"CUSTOMERS: {CUSTOMERS}")
print (f"ORDERS: {ORDERS}")
print (f"PRODUCTS: {PRODUCTS}")
print (f"PAYMENTS: {PAYMENTS}")


