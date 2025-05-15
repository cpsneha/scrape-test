#Assignment: scraping details of samsung mobiles on flipkart priced below 60k


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

base_url = "https://www.flipkart.com/search?q=samsung+mobiles+price+below+60000+rupees&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}"
ua = UserAgent()
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

pages =100 

for page in range(1, pages + 1):
    url = base_url.format(page)

    print(f"\n--- Page {page} ---\n")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    
    names = soup.find_all("div", class_="KzDlHZ")
    prices = soup.find_all("div", class_="Nx9bqj _4b5DiR")

    
    for name_tag, price_tag in zip(names, prices):
        name = name_tag.get_text(strip=True)
        price_text = price_tag.get_text(strip=True).replace("₹", "").replace(",", "")

        try:
            price = int(price_text)
            if price <= 60000:
                print(f"Name: {name} - Price: ₹{price}")
        except ValueError:
            continue

    


