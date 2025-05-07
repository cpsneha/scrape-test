#pgm to get model name and make name from list

import requests
from fake_useragent import UserAgent

api_url="https://www.carwale.com/api/v4/autocomplete/?source=1%2C2%2C3%2C5%2C11%2C15%2C13%2C14%2C10%2C16%2C17%2C4%2C8%2C9%2C6%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29&value=mahindra&size=20&applicationId=1&showNoResult=true&cityId=-1"
ua = UserAgent()
header= { "User-Agent":ua.random}

response=requests.get(api_url,headers=header)
data=response.json()
#print(data)
filter_data=[]
for item in data:
    items={
        "model_name":item["payload"].get("modelName"),
        "makeName":item["payload"].get("makeName")
        }
    filter_data.append(items)
for model_name in filter_data:
    print(model_name)
