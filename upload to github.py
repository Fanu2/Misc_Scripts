import os
from github import Github
from github import InputGitAuthor

# Configuration
token = 'your_github_token'
repo_name = 'beautiful-webpage'
file_paths = ['index.html', 'styles.css']
commit_message = 'Initial commit with beautiful webpage'

# Authenticate with GitHub
g = Github(token)
user = g.get_user()

# Create a new repository
repo = user.create_repo(repo_name, private=False)

# Add files to the repository
for file_path in file_paths:
    with open(file_path, 'r') as file:
        content = file.read()
    repo.create_file(file_path, commit_message, content)

print(f"Files uploaded to GitHub repository '{repo_name}'")
