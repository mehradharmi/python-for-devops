import os
import boto3

def create_bucket(bucket_name, file_name, region):
    s3 = boto3.client("s3")
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

        backup_file_name = file_name + ".bak"
        os.rename(file_name, backup_file_name)

        try:
            s3.upload_file(
                backup_file_name,
                bucket_name,
                file_name
            )
            print(f"{file_name} uploaded successfully to to {bucket_name}")
        except Exception as e:
            print("Error in uploading")

create_bucket("dharmi-lngodium", "s3_bucket.py", "us-west-1")