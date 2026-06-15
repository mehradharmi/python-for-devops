response = {
    "Projects": [
        {
            "ProjectName": "DevOps",
            "Servers": [
                {
                    "Name": "web01",
                    "Services": [
                        {"Name": "nginx"},
                        {"Name": "docker"}
                    ]
                },
                {
                    "Name": "db01",
                    "Services": [
                        {"Name": "mysql"}
                    ]
                }
            ]
        },
        {
            "ProjectName": "Monitoring",
            "Servers": [
                {
                    "Name": "monitor01",
                    "Services": [
                        {"Name": "prometheus"},
                        {"Name": "grafana"}
                    ]
                }
            ]
        }
    ]
}
for project in response["Projects"]:
    print("Project: ", project["ProjectName"])
    for server in project["Servers"]:
        print("Server: ", server["Name"])
        for service in server["Services"]:
            print(service["Name"])