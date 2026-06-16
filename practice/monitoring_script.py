response = {
    "Instances": [
        {"id":"i-101","state":"running"},
        {"id":"i-102","state":"stopped"},
        {"id":"i-103","state":"running"},
        {"id":"i-104","state":"stopped"}
    ]
}
Running_server = []
Stopped_server = []
for instance in response["Instances"]:
    if instance["state"] == "running":
        Running_server.append(instance["id"])
    elif instance["state"] == "stopped":
        Stopped_server.append(instance["id"])
print("Running Server:")
for server in Running_server:
    print(server)
print("\n")
print("Stopped Server:")
for server in Stopped_server:
    print(server)
