import boto3

def create_ec2_instance(ami_id, instance_type, key_name, security_group_id, instance_name, storage_size):
    ec2 = boto3.client("ec2")
    try:
        ec2.run_instances(
            ImageId = ami_id,
            InstanceType = instance_type,
            KeyName = key_name,
            SecurityGroupIds = [security_group_id],
            MinCount = 1,
            MaxCount = 1,
            TagSpecifications = [
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": instance_name
                        }
                    ]
                }
            ],
            BlockDeviceMappings = [
                {
                    "DeviceName": "/dev/xvda",
                    "Ebs": {
                        "VolumeSize": storage_size,
                        "VolumeType": "gp3",
                    }
                }
            ]
        )
        print("ec2 created successfully")
    except Exception as e:
        print(f"Error while creating ec2 instance: {e}")

create_ec2_instance("ami-091138d0f0d41ff90", "t3.micro", "python-script-key", "sg-0c751701477eb02c5", "my-python-ec2", 8)