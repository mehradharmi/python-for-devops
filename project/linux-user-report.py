import subprocess
me = subprocess.run(
    ["whoami"],
    capture_output = True,
    text = True
)

host = subprocess.run(
    ["hostname"],
    capture_output = True,
    text = True
)

tarikh = subprocess.run(
    ["date"],
    capture_output = True,
    text = True
)
tithi = tarikh.stdout.split()

print("System Report\n")
print(f"User: {me.stdout.strip()}")
print(f"Hostname: {host.stdout}")
print(f"Date: {tithi[1]} {tithi[2]} {tithi[3]}")
print(f"Time: {tithi[4]} {tithi[5]}")
print(f"Timezone: {tithi[6]}")