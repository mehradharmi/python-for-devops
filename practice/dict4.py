"""  print i-111 running

i-222 stopped
"""


response = {
    "Reservations": [
        {
            "Instances": [
                {
                    "InstanceId": "i-111",
                    "State": {
                        "Name": "running"
                    }
                },
                {
                    "InstanceId": "i-222",
                    "State": {
                        "Name": "stopped"
                    }
                }
            ]
        }
    ]
}
for instance in response["Reservations"][0]["Instances"]:
    print(instance["InstanceId"])