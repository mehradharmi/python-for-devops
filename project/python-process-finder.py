import subprocess

data = subprocess.run(
    ["ps", "-e"],
    capture_output = True,
    text = True
)
i = 0
lines = data.stdout.splitlines()
for line in lines[1:]:
    process = line.split()

    if process[3] == "python3" or process[3] == "python":
        i += 1
        print(f"Python process {i}: {process[3]}")
print(f"Total Python processes: {i}")