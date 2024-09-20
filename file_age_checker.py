import os
import time

def check_file_age(directory, days):
    cutoff = time.time() - days * 86400
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            if os.path.getmtime(file_path) < cutoff:
                print(f"{filename} is older than {days} days")

if __name__ == "__main__":
    check_file_age('/path/to/directory', 30)