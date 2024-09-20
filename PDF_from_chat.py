import os
import pdfkit

# Define the directory containing HTML files
directory = '/home/jasvir/Documents/Medicine GPT/'

# List all HTML files in the directory
html_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.html')]

# Check if there are any HTML files
if not html_files:
    print("No HTML files found in the directory.")
    exit(1)

# Options to handle different scenarios
options = {
    'enable-local-file-access': '',  # Allow local file access
    'enable-javascript': '',  # Enable JavaScript
    'no-stop-slow-scripts': '',  # Prevent timeout issues with slow scripts
    'javascript-delay': 2000,  # Add a delay to ensure JavaScript execution is complete
    'load-error-handling': 'ignore',  # Ignore load errors
    'disable-external-links': '',  # Ignore external links
    'disable-smart-shrinking': '',  # Prevent shrinking content to fit the page
}

# Process each HTML file separately
for html_file in html_files:
    output_pdf = os.path.splitext(html_file)[0] + '.pdf'
    try:
        pdfkit.from_file(html_file, output_pdf, options=options)
        print(f"PDF generated successfully: {output_pdf}")
    except Exception as e:
        print(f"An error occurred while generating the PDF for {html_file}: {e}")
