# Write file
"""with open("servers.txt", "a") as file:
    server = file.write("\ndb01")
"""

# Read file
"""with open("servers.txt", "r") as file:
    data = file.read()
    print(data)"""

with open("servers.txt") as file:
    for server in file:
        server = server.strip()
        print(f"connecting to server {server}")