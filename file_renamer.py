import os

def rename_files(directory, prefix='new_', suffix=''):
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path):
            new_name = prefix + filename + suffix
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} to {new_name}")

if __name__ == "__main__":
    rename_files('/path/to/directory')