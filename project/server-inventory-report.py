response = {
    "Instances": [
        {"id": "i-101", "state": "running", "cpu": 35},
        {"id": "i-102", "state": "stopped", "cpu": 0},
        {"id": "i-103", "state": "running", "cpu": 82},
        {"id": "i-104", "state": "running", "cpu": 15}
    ]
}

print("Server Inventory Report")
running_server = []
stopped_server = []
total_running = 0
total_stopped = 0
high_cpu = []
for instance in response["Instances"]:
    if instance["state"] == "running":
        running_server.append(f"{instance['id']} {instance['cpu']}%")
        total_running += 1
    elif instance["state"] == "stopped":
        stopped_server.append(instance["id"])
        total_stopped += 1

for instance in response["Instances"]:
    if instance["cpu"] > 80:
        high_cpu.append(instance["id"])
print("Running Server")
for server in running_server:
    print(server)
print("\n")
print("Stopped Server")
for server in stopped_server:
    print(server)
print("\n")
print(f"Total Running: {total_running}")
print(f"Total Stopped: {total_stopped}")
print("\n")
print("High CPU Servers (>80%):")
for cpu in high_cpu:
    print(cpu)