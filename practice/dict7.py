# Target Output
"""Region: us-west-1
Instance: i-111
Volume Size: 20

Region: us-west-1
Instance: i-111
Volume Size: 50"""

response = {
    "Regions": [
        {
            "Name": "us-west-1",
            "Instances": [
                {
                    "InstanceId": "i-111",
                    "Volumes": [
                        {"Size": 20},
                        {"Size": 50}
                    ]
                }
            ]
        }
    ]
}
for region in response["Regions"]:

    for instance in region["Instances"]:

        for volume in instance["Volumes"]:

            print("Region:", region["Name"])
            print("Instance:", instance["InstanceId"])
            print("Volume Size:", volume["Size"])
            print()