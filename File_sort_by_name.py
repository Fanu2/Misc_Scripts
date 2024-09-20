import os
import shutil

# Define the directory containing the files
directory = '/home/jasvir/Books/Books/'

# Ensure the directory exists
if not os.path.isdir(directory):
    raise FileNotFoundError(f"Directory '{directory}' does not exist.")

# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # Skip if it's a directory
    if os.path.isdir(file_path):
        continue

    # Create a subfolder named after the file's name (excluding extension)
    folder_name = os.path.splitext(filename)[0]
    subfolder_path = os.path.join(directory, folder_name)

    # Create the subfolder if it doesn't exist
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    # Move the file into the subfolder
    shutil.move(file_path, os.path.join(subfolder_path, filename))

print("Files have been sorted and moved into respective folders.")
