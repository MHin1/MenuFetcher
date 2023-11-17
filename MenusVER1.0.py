import requests
from bs4 import BeautifulSoup
import os
import subprocess

# Function to check internet connectivity
def check_internet_connection():
    try:
        # Try to send a GET request to a well-known website (e.g., Google)
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Check internet connectivity
if not check_internet_connection():
    print("No Connection. Please connect to the internet.")
    input("Press Enter to continue...")
    exit()

# Define website URLs and names
websites = [
    {'url': 'https://lounasravintolamaku.fi/lounasmenu/', 'name': 'lounasravintolamaku.fi'},
    {'url': 'https://koskenhelmi.fi/lounaslista/', 'name': 'koskenhelmi.fi'},
]

# Create the output directory if it doesn't exist
output_directory = 'D:/Menus'
os.makedirs(output_directory, exist_ok=True)

for website in websites:
    # Send an HTTP GET request to the website URL
    response = requests.get(website['url'])

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize variables to store scraped data
        menu_date_items = []
        additional_info = None

        # Scrape data based on website structure
        if 'lounasravintolamaku.fi' in website['url']:
            # Add the website name at the top
            menu_date_items.append(f'Website: {website["name"]}')
            
            # Find all h4 elements with class 'output_title' for menu date and items
            menu_elements = soup.find_all('h4', class_='output_title')

            # Iterate through menu elements and corresponding menu items
            for menu_element in menu_elements:
                menu_date = menu_element.text.strip()
                menu_items_list = menu_element.find_next('ul')

                if menu_items_list:
                    menu_items = menu_items_list.find_all('li')
                    menu_items_text = [f'- {menu_item.text.strip()}' for menu_item in menu_items]
                    menu_date_items.append(f'Menu Date: {menu_date}\n' + '\n'.join(menu_items_text))

        elif 'koskenhelmi.fi' in website['url']:
            # Find all div elements with class 'lounassivu-otsikko' for menu date and items
            menu_elements = soup.find_all('div', class_='lounassivu-otsikko')

            # Find the div with additional information
            additional_info_element = soup.find('div', class_='mt-4')

            if additional_info_element:
                additional_info = additional_info_element.text.strip()

            # Iterate through menu elements and corresponding pricing and dietary information
            for menu_element in menu_elements:
                menu_date = menu_element.text.strip()
                
                # Check if the ul element exists before trying to find li elements
                menu_items_list = menu_element.find_next('div', class_='lounassivu-lounas')
                if menu_items_list:
                    menu_items_text = menu_items_list.get_text(separator='\n', strip=True)
                    menu_date_items.append(f'{menu_date}\n{menu_items_text}')

        # Combine all scraped data into a single string
        combined_data = '\n\n'.join(menu_date_items)
        if additional_info:
            combined_data = f'{website["name"]}:\nAdditional Information:\n{additional_info}\n\n{combined_data}'

        # Create a filename based on the website name
        filename = os.path.join(output_directory, f'{website["name"]}.txt')

        # Write the combined data to the output file
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(combined_data)
            print(f'Successfully scraped data from {website["url"]} and saved to {filename}')
        except UnicodeEncodeError:
            print(f'Failed to write data to {filename}. UnicodeEncodeError.')

    else:
        print(f'Failed to retrieve data from {website["url"]}. Status code: {response.status_code}')

# Run additional scripts
scripts_to_run = ["MenusVER1.0C1.py", "MenusVER1.0C2.py", "MenusVER1.0C3.py"]

for script in scripts_to_run:
    script_path = os.path.join("D:/Pythoni", script)
    subprocess.run(["python", script_path])

print("All scripts have been executed.")

input("Press Enter to continue...")