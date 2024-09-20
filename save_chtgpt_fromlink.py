import requests
import os

# URL of the file to download
url = "https://chatgpt.com/share/50e9262a-d007-4eaa-bed5-215d382640b7"

# Base path where the content will be saved
base_path = "/home/jasvir/Documents/Medicine GPT/"
base_filename = "saved_content"
extension = ".html"

# Combine base path and filename to create the full file path
save_path = os.path.join(base_path, base_filename + extension)

# Check if the file already exists and rename if necessary
if os.path.exists(save_path):
    i = 1
    while os.path.exists(os.path.join(base_path, f"{base_filename}_{i}{extension}")):
        i += 1
    save_path = os.path.join(base_path, f"{base_filename}_{i}{extension}")

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to a file
        with open(save_path, 'w') as file:
            file.write(response.text)
        print(f"Content successfully saved to {save_path}")
    else:
        print(f"Failed to retrieve the content. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
