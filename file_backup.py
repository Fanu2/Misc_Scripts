import os
import shutil
from datetime import datetime

def backup_files(directory, backup_dir):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}')
    os.makedirs(backup_path, exist_ok=True)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            shutil.copy2(file_path, backup_path)
            print(f"Backed up: {filename} to {backup_path}")

if __name__ == "__main__":
    backup_files('/path/to/directory', '/path/to/backup_dir')