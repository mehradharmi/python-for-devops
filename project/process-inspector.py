import subprocess 

data = subprocess.run(
    ["ps", "-e"],
    capture_output = True,
    text = True
)
i = 0
#print(data.stdout)
lines = data.stdout.splitlines()
print("Process Report\n")
for line in lines [1:]:
    parts = line.split()
    i += 1
    print(f"Process {i}: {parts[3]}")

print("\n")
print(f"Toatl process: {i}")