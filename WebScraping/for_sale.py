import random
from flask import Flask
from pymongo import MongoClient
import json
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# MongoDB configuration using your connection string
client = MongoClient("mongodb+srv://lagnarokthor:berkaypehlivan2001@cluster1.upejjdz.mongodb.net/?retryWrites=true&w=majority&appName=cluster1")
db = client['house_info']  # Use 'house_info' as the database name
collection = db['for_sale1']  # Use 'for_sale' as the collection name

base_url = "https://dovecconstruction.com/en/property-for-sale/"

# List of cities
cities = ['Nicosia', 'Kyrenia', 'Güzelyurt', 'Famagusta', 'Lefke']

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

        short_description_elem = desc.find('p')
        if short_description_elem:
            short_description = short_description_elem.text.strip()
        else:
            short_description = "N/A"


        # Randomly select a city
        city = random.choice(cities)

        house_info = {
            "title": title,
            "price": price,
            "closed_area": closed_area,
            "bedrooms": bedroom,
            "bath_wc": bath_wc,
            "item_status": item_status,
            "short_description": short_description,
            "city": city
        }

        # Insert house info into MongoDB
        collection.insert_one(house_info)

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

# Close MongoDB connection after scraping
client.close()

@app.route('/')
def index():
    return "Scraping completed. House information with city info saved to MongoDB."

if __name__ == '__main__':
    app.run(debug=True)
