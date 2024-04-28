import json
import requests
from bs4 import BeautifulSoup

base_url = "https://dovecconstruction.com/en/property-for-sale/"
houses = []

def extract_house_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    descriptions = soup.find_all('div', class_='description')

    for desc in descriptions:
        title_elem = desc.find('h3', class_='title')
        if title_elem:
            title = title_elem.text.strip()
        else:
            title = "N/A"

        price_elem = desc.find('span', class_='current')
        if price_elem:
            price = price_elem.text.strip()
        else:
            price = "N/A"

        closed_area_elem = desc.find('span', string='Closed area').find_next_sibling('span')
        if closed_area_elem:
            closed_area = closed_area_elem.text.strip()
        else:
            closed_area = "N/A"

        bedroom_elem = desc.find('span', string='Bedroom').find_next_sibling('span')
        if bedroom_elem:
            bedroom = bedroom_elem.text.strip()
        else:
            bedroom = "N/A"

        bath_wc_elem = desc.find('span', string='Bath/Wc').find_next_sibling('span')
        if bath_wc_elem:
            bath_wc = bath_wc_elem.text.strip()
        else:
            bath_wc = "N/A"

        item_status_elem = desc.find('span', string='Item Status').find_next_sibling('span')
        if item_status_elem:
            item_status = item_status_elem.text.strip()
        else:
            item_status = "N/A"

        house_info = {
            "Title": title,
            "Price": price,
            "Closed Area": closed_area,
            "Bedrooms": bedroom,
            "Bath/Wc": bath_wc,
            "Item Status": item_status
        }

        houses.append(house_info)

page_number = 1
while True:
    page_url = f"{base_url}{page_number}/"
    response = requests.get(page_url)
    if response.status_code == 200:
        html_content = response.content
        extract_house_info(html_content)
        page_number += 1
    else:
        break

with open('houses.json', 'w') as json_file:
    json.dump(houses, json_file, indent=4)

print(f"Scraped {len(houses)} houses. House information saved to 'houses.json' file.")
