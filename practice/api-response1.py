data = {
    "servers": [
        {
            "name": "web1",
            "status": "running"
        },
        {
            "name": "web2",
            "status": "stopped"
        },
        {
            "name": "web3",
            "status": "running"
        }
    ]
}
for server in data["servers"]:
    if server["status"] == "running":
        print(server["name"])