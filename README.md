## Team Members
- Berkay Pehlivan
- Kaan Acar
- Mehmet Oktar Onder


# Dovecs Property Marketing Solution

This project is developed by Group 8 as part of the 2023-2024 hackathon in TRNC Famagusta. It features an AI-driven chatbot integrated with Dovecs' website to enhance customer interactions and improve property marketing strategies.




https://github.com/Strong-Moon/Hackathon/assets/110940123/8511d024-7294-435a-81ae-3b4058bd9604




## Introduction
The solution focuses on leveraging automation, data analysis, and personalized communication to address the marketing challenges faced by Dovecs. It utilizes technologies like web scraping, MongoDB, and SMS notifications to provide real-time updates and efficiently manage customer data.

## Features
- **AI Chatbot**: Engages with customers directly on the Dovecs website, providing tailored interactions.
- **Web Scraping**: Uses BeautifulSoup to scrape real-time house details directly from web sources.
- **Database Management**: Utilizes MongoDB for efficient data storage and retrieval.
- **SMS Notifications**: Sends targeted property details to potential customers via SMS, expanding the marketing reach.

# Implementation

## Web Scraping
- Libraries used: `json`, `requests`, `BeautifulSoup`
- Connects to MongoDB and retrieves house information from specified URLs.
  ```bash
  mongodb+srv://<username>:<password>@cluster1.upejjdz.mongodb.net/?retryWrites=true&w=majority&appName=cluster1
- Two base URLs that we want to scrape should be provided.
  ```bash
  base_sale_url = "https://dovecconstruction.com/en/property-for-sale/"
  base_rent_url = "https://dovecconstruction.com/en/property-for-rent/"
  
### Code Snippets

Below is a shortened example of the `extract_house_info` function used for scraping and storing house details from HTML content into MongoDB:

```python
def extract_house_info(html, collection):
    soup = BeautifulSoup(html, 'html.parser')
    descriptions = soup.find_all('div', class_='description')

    for desc in descriptions:
        # Extracting house attributes
        title = desc.find('h3', class_='title').text.strip() if desc.find('h3', class_='title') else "N/A"
        price = desc.find('span', class_='current').text.strip() if desc.find('span', class_='current') else "N/A"
        closed_area = desc.find('span', string='Closed area').find_next_sibling('span').text.strip() if desc.find('span', string='Closed area') else "N/A"
        bedroom = desc.find('span', string='Bedroom').find_next_sibling('span').text.strip() if desc.find('span', string='Bedroom') else "N/A"
        bath_wc = desc.find('span', string='Bath/Wc').find_next_sibling('span').text.strip() if desc.find('span', string='Bath/Wc') else "N/A"
        item_status = desc.find('span', string='Item Status').find_next_sibling('span').text.strip() if desc.find('span', string='Item Status') else "N/A"
        short_description = desc.find('p').text.strip() if desc.find('p') else "N/A"

        # Generating unique ID and assigning city randomly
        city = random.choice(cities)
        v_id = str(uuid.uuid4())

        # Creating house info dictionary
        house_info = {
            "title": title,
            "price": price,
            "closed_area": closed_area,
            "bedrooms": bedroom,
            "bath_wc": bath_wc,
            "item_status": item_status,
            "short_description": short_description,
            "city": city,
            "v_id": v_id 
        }

        # Inserting into MongoDB
        collection.insert_one(house_info)

```
For the scrapping of the properties `scrape_properties` function was used. The first parameter is our base urls that we provided in the first and the second parameter takes our collections names that are located int the database.

```python
def scrape_properties(base_url, collection):
    page_number = 1
    while True:
        page_url = f"{base_url}{page_number}/"
        response = requests.get(page_url)
        if response.status_code == 200:
            html_content = response.content
            extract_house_info(html_content, collection)
            page_number += 1
        else:
            break
```
The main problem was the move to other pages. Thanks to this function this problem is solved after many trials.

```python
scrape_properties(base_sale_url, collection_sale)
scrape_properties(base_rent_url, collection_rent)
client.close()
```
The last part is calling our function with its parameters, after that closing MongoDB connection after scraping.

### SMS Notifications
- MongoDB setup to retrieve and manage customer and property data.
- Integration with Twilio API to send SMS messages based on user preferences and inquiries.

### AI Chatbot
- Developed using Flask for the backend.
- Utilizes language processing to interact and respond to user queries effectively.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-github-username/dovecs-property-marketing.git
