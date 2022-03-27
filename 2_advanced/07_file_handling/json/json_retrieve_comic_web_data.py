
import json
import requests
from datetime import datetime
today = datetime.today().strftime('%Y-%m-%d')


def return_status(link):
    status_response = requests.get(link).status_code
    return status_response


def retrieve_data(link):
    response = requests.get(link)
    data = json.loads(response.text)
    return data
    

if __name__ == '__main__':
    print(today)
    status = return_status('https://xkcd.com/info.0.json')
    data = retrieve_data('https://xkcd.com/info.0.json')
    print(status, data)


