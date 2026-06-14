import os


def run_command(command):
    return os.system(command)

run_command("df -h")  # Linux df -h command to check disk space

print("")

run_command('uptime')   # uptime and load average