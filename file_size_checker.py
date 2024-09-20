import os

def file_sizes(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            print(f"{filename}: {size} bytes")

if __name__ == "__main__":
    file_sizes('/path/to/directory')