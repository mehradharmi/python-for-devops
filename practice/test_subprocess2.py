import subprocess

today = subprocess.run(
    ["date"],
    capture_output=True,
    text=True
)

print(today.stdout)
result = today.stdout.split()

date = f"{result[1]}-{result[2]}-{result[3]}"
time = f"{result[4]}:{result[5]}"
timezone = f"{result[6]}"
print("TODAY :" ,date)
print("TIME: ", time)
print("TIMEZONE:", timezone)