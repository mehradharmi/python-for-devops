response = {
    "Instances": [
        {"id":"i-101","state":"running"},
        {"id":"i-102","state":"stopped"},
        {"id":"i-103","state":"running"},
        {"id":"i-104","state":"stopped"}
    ]
}
running_server = []
stopped_server = []
for instance in response["Instances"]:
    if instance["state"] == "running":
        running_server.append(instance["id"])
    elif instance["state"] == "stopped":
        stopped_server.append(instance["id"])
print("Running Server:")
for server in running_server:
    print(server)
print("\n")
print("Stopped Server:")
for server in stopped_server:
    print(server)
