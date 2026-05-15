import sys
sys.path.insert(0,'/Workspace/Repos/mushroomred933@gmail.com/ecommerce-data-platform/')

from utils.constants import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    BUCKET,
    REGION
)

print (f"AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID}")
print (f"AWS_SECRET_ACCESS_KEY: {AWS_SECRET_ACCESS_KEY}")
print (f"BUCKET: {BUCKET}")
print (f"REGION: {REGION}")