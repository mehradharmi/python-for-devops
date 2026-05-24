server = {
    "name": "web1",
    "cpu": 92,
    "memory": 70
}

if server["cpu"] > 90:
    print(f"{server['name']} CPU Critical")
