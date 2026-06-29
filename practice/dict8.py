server = {
    "id": "i-101",
    "state": "running",
    "cpu": 35,
    "region": "ap-south-1"
}


server["cpu"] = 65

server["os"] = "Ubuntu 24.04"
for key, value in server.items():
    print(key, value)