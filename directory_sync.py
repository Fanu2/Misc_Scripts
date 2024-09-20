import os
import shutil

def sync_directories(src_dir, dest_dir):
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dest_file = os.path.join(dest_dir, filename)
        if os.path.isfile(src_file):
            if not os.path.exists(dest_file):
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {filename} to {dest_dir}")

if __name__ == "__main__":
    sync_directories('/path/to/source_dir', '/path/to/dest_dir')