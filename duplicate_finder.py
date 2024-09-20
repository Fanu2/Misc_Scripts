import os
import hashlib

def hash_file(file_path):
    """Returns the SHA-256 hash of the file."""
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read the file in chunks to handle large files
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def find_and_remove_duplicates(directory):
    """Finds and removes duplicate files in the given directory."""
    files_seen = {}  # Dictionary to store file hashes and their corresponding paths
    duplicates = []  # List to store the paths of duplicate files

    # Traverse through the directory
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_hash = hash_file(file_path)  # Hash the current file
                if file_hash in files_seen:
                    # Duplicate found
                    duplicates.append(file_path)
                    print(f"Duplicate found: {file_path} (same as {files_seen[file_hash]})")
                    os.remove(file_path)  # Remove the duplicate file
                    print(f"Deleted: {file_path}")
                else:
                    # Store file hash and its path
                    files_seen[file_hash] = file_path
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    print("\nProcess completed. Found and removed duplicates.")

if __name__ == "__main__":
    find_and_remove_duplicates('/home/jasvir/Books/')
