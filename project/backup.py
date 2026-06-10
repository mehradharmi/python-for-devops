import os
import shutil
import datetime

def create_backup(source, detination):
    today = datetime.datetime.now()
    base_path = os.path.join(destination, f"backup-{today}")
    print(f"Backup file is: ",base_path)

    print("making backups........")

    final_path = shutil.make_archive(base_path, "gztar", source)
    print(f"successful backup file to: {final_path}")
    
destination = "/home/dharmi/python-for-devops/project/backups"
source = "/home/dharmi/python-for-devops/project/"
create_backup(source, destination)
