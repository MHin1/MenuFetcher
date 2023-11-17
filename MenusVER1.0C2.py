import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the website
url = 'https://neste-aanekoski.fi/417138177'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <p> elements with class 'mobile-oversized'
    p_elements = soup.find_all('p', class_='mobile-oversized')

    # Create a directory to save the scraped data
    output_directory = 'D:/Menus'  # Change this to your desired save location
    os.makedirs(output_directory, exist_ok=True)

    # Create a filename
    filename = os.path.join(output_directory, 'neste.fi.txt')

    # Open the output file for writing with 'iso-8859-1' encoding
    with open(filename, 'w', encoding='iso-8859-1') as file:
        # Write "neste.fi" at the top of the file
        file.write("neste.fi\n\n")
        
        # Iterate through <p> elements
        for p_element in p_elements:
            # Extract and write the text content
            file.write(p_element.text.strip() + '\n')

    # Print a message to indicate successful scraping
    print(f'Successfully scraped data from {url} and saved to {filename}')

else:
    print(f'Failed to retrieve data from {url}. Status code: {response.status_code}')
