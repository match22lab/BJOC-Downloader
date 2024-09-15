import os
import requests
import time

# This script saves all articles published in Beilstein J. Org. Chem in a designated folder

# Designated folder to save PDFs
folder = r'C:\Users\match\Desktop\Beilstein PDFs'
if not os.path.exists(folder):
    os.makedirs(folder)

# Custom headers to mimic a browser request
headers = {'User-Agent': 'Mozilla/5.0 (compatible; Python script for downloading PDFs)'}

# Loop over volumes (XX) from 1 to 22
for volume in range(1, 22):  # 1 to 22 inclusive
    # Loop over articles (YYY) from 1 to 340
    for article in range(1, 340):  # 1 to 340 inclusive
        # Construct the URL
        url = f'https://www.beilstein-journals.org/bjoc/content/pdf/1860-5397-{volume}-{article}.pdf'
        # Construct the filename to save
        filename = f'1860-5397-{volume}-{article}.pdf'
        filepath = os.path.join(folder, filename)
        # Check if file already exists
        if os.path.exists(filepath):
            print(f"File {filename} already exists. Skipping.")
            continue
        # Make the request
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                # Save the PDF file
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {filename}")
            elif response.status_code == 404:
                print(f"{filename} not found (404). Skipping.")
            else:
                print(f"Error {response.status_code} for {filename}.")
            # Be polite to the server
            time.sleep(0.1)
        except requests.exceptions.RequestException as e:
            print(f"Request exception for {filename}: {e}")
            time.sleep(1)
