from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get('https://dovecconstruction.com/en/property-for-sale/').text
    soup = BeautifulSoup(html_text, 'lxml')

    houses = soup.find_all('div', class_="description")

    for house in houses:
        house_name = house.find("h3", class_ = "title").text # use it just in case .replace(" ","")
        house_price = house.find("span", class_ = "current").text.replace(" ","")
        # house_closed_area = house.find("span", class_="name").text
        house_closed_area_val = house.find("span", class_="attr").text
        house_bedroom = house.find("span", class_="attr").text
        house_link = house.div.a
        print(f"Name: {house_name.strip()}")
        print(f"Price: {house_price.strip()}")
        print(f"Closed Area: {house_closed_area_val.strip()}")
        print(f"Link: {house_link}")



def main():
    print("Hello World!")

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        # print(f"Waiting {time_wait} minutes..")
        time.sleep(time_wait * 60) #repeat every 10 min
















""" 
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://dovecconstruction.com/en/property-for-sale/').text
soup = BeautifulSoup(html_text, 'lxml')

house = soup.find('div', class_="description")
house_name = house.find("h3", class_ = "title").text # use it just in case .replace(" ","")
house_price = house.find("span", class_ = "current").text.replace(" ","")
# house_closed_area = house.find("span", class_="name").text
house_closed_area_val = house.find("span", class_="attr").text
house_bedroom = house.find_next("span", class_="attr").text
print(house_bedroom)
# house_bath 
# house_item_status 


print(f'''
Name: {house_name}
Price: {house_price}
Closed Area: {house_closed_area_val}
''')

# print(house_name)
# print(house_price)
# print(house_closed_area)
# print(house_closed_area_val) 
"""



""" 
html_text = requests.get('https://dovecconstruction.com/en/property-for-sale/').text
soup = BeautifulSoup(html_text, 'lxml')

houses = soup.find_all('div', class_="description")

for house in houses:
    house_name = house.find("h3", class_ = "title").text # use it just in case .replace(" ","")
    house_price = house.find("span", class_ = "current").text.replace(" ","")
    # house_closed_area = house.find("span", class_="name").text
    house_closed_area_val = house.find("span", class_="attr").text
    house_bedroom = house.find_next("span", class_="attr").text
    print(f'''
        Name: {house_name}
        Price: {house_price}
        Closed Area: {house_closed_area_val}
        ''')
    print("----------------")
 """