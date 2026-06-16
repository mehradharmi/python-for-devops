response = {
    "Instances": [
        {"id":"i-101","state":"running"},
        {"id":"i-102","state":"stopped"},
        {"id":"i-103","state":"running"}
    ]
}
print("Running Servers:\n")
for instance in response["Instances"]:
    if instance["state"] == "running":
        print(instance["id"])