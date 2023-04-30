import requests 
import json 

def create_bucket():

    url = "http://127.0.0.1:8000/stock-update/IBM/Apr 03, 2023"

    headers = {
        "content-type": "application/json"
    }

    params = {
        
        "adj_close": 132.06,
        "close": 132.06,
        "company": "IBM",
        "date": "Apr 03, 2023",
        "high": 132.61,
        "low": 132.61,
        "open": 130.97,
        "volume": "3,840,100"
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(params))

    print(response.json())

create_bucket()