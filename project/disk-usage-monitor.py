import subprocess
data = subprocess.run(
    ["df", "-h"],
    capture_output = True,
    text = True
)
print("Disk Usage Report\n")
memory = data.stdout.splitlines()
parts = memory[2].split()
print(f"Filesystem: {parts[0]}\nSize: {parts[1]}\nUsed: {parts[2]}\nAvailable: {parts[3]}\nUsage: {parts[4]}\n")
value = parts[4].replace('%', '')
val = int(value)
if val < 80:
    print("Status: Healthy")
else:
    print("Status: Unhealthy")