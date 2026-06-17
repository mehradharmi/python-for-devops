import subprocess
data = subprocess.run(
    ["ls"],
    capture_output = True,
    text = True
)
i = 0
files = data.stdout.splitlines()
print("Directory Report\n")
for file in files:
    i += 1
    print(f"Item {i}: {file}")
print("\n")
print(f"Total Items: {i}")