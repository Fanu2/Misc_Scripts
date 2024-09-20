import os
import shutil


def organize_files(source_dir):
    print(f"Checking directory: {source_dir}")

    if not os.path.exists(source_dir):
        print(f"Directory {source_dir} does not exist!")
        return

    # Traverse all files and directories recursively
    for dirpath, dirnames, filenames in os.walk(source_dir):
        # Process each file
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            print(f"Processing file: {file_path}")

            # Get the file extension and move the file to its respective folder
            if '.' in filename:
                ext = filename.split('.')[-1]
                target_dir = os.path.join(source_dir, ext)

                # Create the target directory if it doesn't exist
                os.makedirs(target_dir, exist_ok=True)

                # Define the target file path
                target_file_path = os.path.join(target_dir, filename)

                # If a file with the same name already exists, rename the file to avoid conflict
                if os.path.exists(target_file_path):
                    base_name, extension = os.path.splitext(filename)
                    new_filename = f"{base_name}_duplicate{extension}"
                    target_file_path = os.path.join(target_dir, new_filename)
                    print(f"Renaming to avoid conflict: {new_filename}")

                # Move the file
                shutil.move(file_path, target_file_path)
                print(f"Moved: {filename} to {target_dir}")
            else:
                print(f"Skipped: {filename} (No extension)")

    # Now check for empty directories
    for dirpath, dirnames, filenames in os.walk(source_dir, topdown=False):
        # Remove any empty directories
        if not os.listdir(dirpath):
            os.rmdir(dirpath)
            print(f"Deleted empty directory: {dirpath}")


if __name__ == "__main__":
    organize_files('/media/jasvir/My Passport/Family/jass/')
