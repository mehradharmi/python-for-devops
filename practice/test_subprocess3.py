import subprocess

memory = subprocess.run(
    ["df", "-h"],
    capture_output = True,
    text = True
)
print(memory.stdout)