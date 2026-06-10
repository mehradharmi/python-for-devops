"""
this script is for backup from local to s3 bucket
"""

import boto3
import os
import datetime
import shutil


def create_bucket(bucket_name, file_name, region):
    s3 = boto3.client("s3")
    try:

        s3.create_bucket(
            Bucket = bucket_name,
            CreateBucketConfiguration = {
                "LocationConstraint": region
                }
            )
        print(f"Bucket: {bucket_name} created successfully")

    except Exception as e:
        print(f"Error occurred: {e}")

        today = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

        name, ext = os.path.splitext(file_name)

        backup_file = os.path.join(name, f"backup-{today}{ext}")
        print(f"Backup file is: {backup_file}")
    try:

        s3.upload_file(
            file_name,
            bucket_name,
            backup_file
            )
        print(f"File {backup_file} uploaded successfully")
    except Exception as e:
        print(f"Error occurred during file upload: {e}")


create_bucket("lindodium-backup-2026", "backup.py", "us-west-1")
