import boto3
import os
import datetime


def create_bucket(bucket_name, file_name, region):

    s3 = boto3.client(
        "s3",
        region_name=region
    )

    # Backup file name generate
    timestamp = datetime.datetime.now().strftime(
        "%Y%m%d-%H%M%S"
    )

    name, ext = os.path.splitext(file_name)

    backup_file = f"{name}-{timestamp}{ext}"

    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": region
            }
        )

        print(
            f"Bucket '{bucket_name}' created successfully"
        )

    except Exception as e:
        print(
            f"Bucket may already exist or error occurred: {e}"
        )

    try:
        s3.upload_file(
            file_name,
            bucket_name,
            backup_file
        )

        print(
            f"File uploaded as '{backup_file}'"
        )

    except Exception as e:
        print(
            f"Upload failed: {e}"
        )


create_bucket(
    "lindodium-backup-2026",
    "backup.py",
    "us-west-1"
)