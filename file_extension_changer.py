import os

def change_file_extension(directory, old_ext, new_ext):
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            base = filename[:-len(old_ext)]
            new_filename = base + new_ext
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} to {new_filename}")

if __name__ == "__main__":
    change_file_extension('/path/to/directory', '.txt', '.md')