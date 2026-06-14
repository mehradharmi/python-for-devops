# Task Print
"""Bucket: backup-prod

app.zip
db.zip

Bucket: backup-dev

test.zip"""


response = {
    "Buckets": [
        {
            "Name": "backup-prod",
            "Files": [
                {
                    "FileName": "app.zip",
                    "Size": 100
                },
                {
                    "FileName": "db.zip",
                    "Size": 200
                }
            ]
        },
        {
            "Name": "backup-dev",
            "Files": [
                {
                    "FileName": "test.zip",
                    "Size": 50
                }
            ]
        }
    ]
}


for bucket in response["Buckets"]:
    print("\nBucket: ",bucket["Name"])
    for file in bucket["Files"]:
        print(file["FileName"])
