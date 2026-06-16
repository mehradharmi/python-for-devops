logs = {
    "entries": [
        "INFO Application Started",
        "ERROR Database Failed",
        "INFO Request Received",
        "ERROR Redis Timeout"
    ]
}
for error in logs["entries"]:
    if "ERROR" in error:
        print(error)