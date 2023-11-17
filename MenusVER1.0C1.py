import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the website you want to scrape
url = 'https://www.caffitella.fi/lounaslista/'

# Create the output directory if it doesn't exist
output_directory = 'D:/Menus'
os.makedirs(output_directory, exist_ok=True)

# Send an HTTP GET request to the website URL
try:
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize variables to store scraped data
        menu_data = {}
        current_day = None

        # Find all <p> elements
        p_elements = soup.find_all('p')

        for p_element in p_elements:
            # Get the text content of the <p> element
            p_text = p_element.get_text(strip=True)

            # Check if the <p> element contains a day name
            if p_text.lower() in ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai"]:
                current_day = p_text
                menu_data[current_day] = []
            elif current_day and p_text:  # Check if there is a current day and the text is not empty
                menu_data[current_day].append(p_text)

        # Find additional information
        additional_info = ""
        for p_element in p_elements:
            if "Päivämäärä:" in p_element.get_text():
                additional_info = p_element.get_text().strip()
                break

        # Combine scraped data into a single string
        combined_data = "Caffitella.fi\n"
        for day, menu_items in menu_data.items():
            combined_data += f"{day}:\n"
            combined_data += "\n".join(menu_items)
            combined_data += "\n\n"
        combined_data += f"Additional Information:\n{additional_info}"

        # Create a filename
        filename = os.path.join(output_directory, 'caffitella.fi.txt')

        # Write the combined data to the output file in 'utf-8' encoding
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(combined_data)

        # Print a message to indicate successful scraping
        print(f'Successfully scraped data from {url} and saved to {filename}')

    else:
        print(f'Failed to retrieve data from {url}. Status code: {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error during the request: {e}')

except Exception as e:
    print(f'An unexpected error occurred: {e}')
