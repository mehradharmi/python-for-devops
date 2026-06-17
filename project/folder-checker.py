import subprocess

folder = input("Enter folder name: ")
data = subprocess.run(
    ["ls", folder],
    capture_output = True,
    text = True
)
status_code = data.returncode
if status_code == 0:
    print("Folder found")
else:
    print("Folder not found")
    print(f"Reason:\n {data.stderr}")