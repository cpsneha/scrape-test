

import requests
from fake_useragent import UserAgent  

api_url = "https://api.nike.com/search/suggestions/v1?country=IN&language=en-gb&count=20"
ua = UserAgent()
user_agent = ua.random


if "Mobile" in user_agent or "iPhone" in user_agent or "Android" in user_agent:
    user_agent = ua.chrome  
else:
    user_agent=user_agent

headers = {"User-Agent": user_agent}

response = requests.get(api_url, headers=headers)
data = response.json()


for item in data["searchTerms"]:
    display_item=item["displayText"]
    print(display_item)










