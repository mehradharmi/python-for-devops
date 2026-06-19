import subprocess
service = input("Enter Service Name: ")

result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output = True,
    text = True
)
print("Service Health Report\n")
print(f"Service: {service}")
status = result.stdout.strip()
if result.returncode == 4 or status == "unknown":
    print(f"{service} is not Available")
elif result.returncode == 0 or status == "active":
    print(f"Status: active\nHealth: OK")
else:
    print(f"Status: inactive\nHealth: NOT OK")