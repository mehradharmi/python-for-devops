server = {
    "id": "i-101",
    "state": {
        "name": "running",
        "code": 16
    },
    "cpu": 35
}
print(f"server id: {server['id']}")
print(server["state"]["name"])
print(f"status code: {server['state']['code']}")

server["cpu"] = 55
print(server["cpu"])

server["state"].update({'name':'stopped', 'code':80})
print(server['state']['name'])

server["state"]["reason"] = "Manual stopped"
print(server['state']['reason'])