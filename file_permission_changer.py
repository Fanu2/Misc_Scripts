import os

def change_permissions(directory, mode):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.chmod(file_path, mode)
            print(f"Changed permissions of: {filename}")

if __name__ == "__main__":
    change_permissions('/path/to/directory', 0o644)