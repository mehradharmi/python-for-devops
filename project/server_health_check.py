servers = [
        {"name": "web01", "cpu": 80},
        {"name": "web02", "cpu": 95},
        {"name": "db01", "cpu": 70}
        ]

for server in servers:
    if server["cpu"] > 90:
        print(f"{server["name"]} is critical")
    else:
        print(f"{server["name"]} is ok")
