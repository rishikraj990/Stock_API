import requests 
import json 

def create_bucket():

    url = "http://127.0.0.1:8000/stock-update/IBM/Apr 03, 2023"
    # url contains http://Domain-Name/stock-update/<COMPANY>/<DATE>

    headers = {
        "content-type": "application/json"
    }

    # Data need to be updated
    params = {
        "adj_close": 132.06,
        "close": 132.06,
        "company": "IBM",
        "date": "Apr 03, 2023",
        "high": 100.61,
        "low": 100.61,
        "open": 130.97,
        "volume": "3,840,100"
    }

    # Send the POST request and collect the response
    response = requests.post(url=url, headers=headers, data=json.dumps(params))

    # Print the response in the terminal of sender
    print(response.json())

#Run the function
create_bucket()