running_count = 0
response = {
    "Instances": [
        {
            "id": "i-101",
            "state": "running"
        },
        {
            "id": "i-102",
            "state": "stopped"
        },
        {
            "id": "i-103",
            "state": "running"
        }
    ]
}
for instance in response["Instances"]:
    print(f"{instance["id"]} is {instance["state"]}")
