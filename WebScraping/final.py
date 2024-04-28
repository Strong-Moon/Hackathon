import json
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://dovecconstruction.com/en/property-for-sale/').text
soup = BeautifulSoup(html_text, 'lxml')

# List to store house information
houses = []

# Extracting information for each description
descriptions = soup.find_all('div', class_='description')

for desc in descriptions:
    title = desc.find('h3', class_='title').text.strip()
    price = desc.find('span', class_='current').text.strip()
    closed_area = desc.find('span', string='Closed area').find_next_sibling('span').text.strip()
    bedroom = desc.find('span', string='Bedroom').find_next_sibling('span').text.strip()
    bath_wc = desc.find('span', string='Bath/Wc').find_next_sibling('span').text.strip()
    item_status = desc.find('span', string='Item Status').find_next_sibling('span').text.strip()

    # Create dictionary for the current house
    house_info = {
        "Title": title,
        "Price": price,
        "Closed Area": closed_area,
        "Bedrooms": bedroom,
        "Bath/Wc": bath_wc,
        "Item Status": item_status
    }

    # Append the dictionary to the list
    houses.append(house_info)

# Write house information to a JSON file
with open('houses.json', 'w') as json_file:
    json.dump(houses, json_file, indent=4)

print("House information saved to 'houses.json' file.")
