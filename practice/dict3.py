response = {
    "Reservations": ["A", "B", "C"]
}

print(response["Reservations"])


response = {
    "Servers": [
        {
            "Name": "web01",
            "CPU": 4
        },
        {
            "Name": "db01",
            "CPU": 8
        }
    ]
}
for server in response["Servers"]:
    print(server["Name"])