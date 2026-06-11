from datetime import datetime
import os
import boto3
import datetime

def create_bucket(bucket_name, file_name, region):
    s3 = boto3.client("s3")
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    name, ext = os.path.splitext(file_name)
    print(f"Name: {name}, Extension: {ext}")

    backup_file = f"{name}-{timestamp}{ext}"
    try:
        s3.create_bucket(
            Bucket = bucket_name,
            CreateBucketConfiguration = {
                "LocationConstraint": region
            }
        )
        print(f"Bucket {bucket_name} created succefully")
    except Exception as e:
        print("bucket may already exists")

        try:
            s3.upload_file(
                file_name,
                bucket_name,
                backup_file
            )
            print(f"{backup_file} uploaded successfully to {bucket_name}")
        except Exception as e:
            print("Error in uploading")

create_bucket("dharmi-lngodium", "server_health_check.py", "us-west-1")