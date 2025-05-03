#scrapping using beautiful soup and applying header



import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

base_url ="https://www.flipkart.com/search?q=samsung%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

ua=UserAgent()
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

}

#print (response)

pages=109
for page in range(1,pages+1):
  url=base_url.format(page)
  response=requests.get(url,headers=headers).text
  data=BeautifulSoup(response,"html.parser")
  items=data.find_all("div",class_="KzDlHZ")
  price=data.find_all("div",class_="Nx9bqj _4b5DiR")


  for mobile_name in items:
    print(mobile_name.get_text(strip=True))
  for mobile_price in price:
    print(mobile_price.get_text(strip=True)) 
