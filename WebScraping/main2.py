from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://dovecconstruction.com/en/property-for-sale/').text
soup = BeautifulSoup(html_text, 'lxml')
# Extracting information for each description
descriptions = soup.find_all('div', class_='description')

for desc in descriptions:
    title = desc.find('h3', class_='title').text.strip()
    price = desc.find('span', class_='current').text.strip()
    closed_area = desc.find('span', string='Closed area').find_next_sibling('span').text.strip()
    bedroom = desc.find('span', string='Bedroom').find_next_sibling('span').text.strip()
    bath_wc = desc.find('span', string='Bath/Wc').find_next_sibling('span').text.strip()
    item_status = desc.find('span', string='Item Status').find_next_sibling('span').text.strip()

    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Closed Area: {closed_area}")
    print(f"Bedrooms: {bedroom}")
    print(f"Bath/Wc: {bath_wc}")
    print(f"Item Status: {item_status}")
    print("------")