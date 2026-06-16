running_count = 0
stopped_count = 0
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
    if instance["state"] == "running":
        running_count += 1
    elif instance["state"] == "stopped":
            stopped_count += 1

print("Running: ", running_count)
print("Stopped: ", stopped_count)