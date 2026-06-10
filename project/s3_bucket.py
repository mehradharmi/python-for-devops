"""
this script is for backup from local to s3 bucket
"""

import boto3


def create_bucket(bucket_name, file_name, region):
    s3 = boto3.client("s3")

    s3.create_bucket(
            Bucket = bucket_name,
            CreateBucketConfiguration = {
                "LocationConstraint": region
                }
            )
    print(f"Bucket: {bucket_name} created successfully")

    s3.upload_file(
            file_name,
            bucket_name,
            file_name
            )
    print("File uploaded succesfully")


create_bucket("lindodium-backup-2026", "backup.py", "us-west-1")
