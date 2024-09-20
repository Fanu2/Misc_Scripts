import os
import subprocess

# Define the project path
project_path = '/home/jasvir/PycharmProjects/Top50AutomationScripts'
scripts_path = os.path.join(project_path, 'scripts')

# Create project directory
os.makedirs(scripts_path, exist_ok=True)

# Initialize a Git repository
subprocess.run(['git', 'init', project_path])

# Create README.md file
with open(os.path.join(project_path, 'README.md'), 'w') as f:
    f.write("# Top 50 Python Scripts for Automation\n")

# Create example scripts
example_scripts = {
    'web_scraper.py': """\
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
""",
    'excel_automation.py': """\
import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False)
""",
    'file_renaming.py': """\
import os

directory = '/path/to/directory'
for filename in os.listdir(directory):
    new_name = filename.replace('old', 'new')
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
""",
    'email_automation.py': """\
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is the body of the email')
msg['Subject'] = 'Test Email'
msg['From'] = 'you@example.com'
msg['To'] = 'friend@example.com'

with smtplib.SMTP('smtp.example.com') as server:
    server.login('username', 'password')
    server.send_message(msg)
""",
    'browser_automation.py': """\
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://example.com')
driver.find_element_by_name('q').send_keys('automation')
driver.find_element_by_name('btnK').click()
"""
}

# Write example scripts to files
for script_name, script_content in example_scripts.items():
    with open(os.path.join(scripts_path, script_name), 'w') as f:
        f.write(script_content)

# Create a virtual environment
subprocess.run(['python3', '-m', 'venv', os.path.join(project_path, 'venv')])

# Install common dependencies within the virtual environment
activate_script = os.path.join(project_path, 'venv/bin/activate')
install_dependencies = f'source {activate_script} && pip install requests beautifulsoup4 pandas openpyxl selenium'
subprocess.run(['bash', '-c', install_dependencies])

print("Project setup complete.")
