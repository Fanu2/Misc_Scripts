import os

def search_files(directory, extension):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))

if __name__ == "__main__":
    search_files('/path/to/directory', '.txt')