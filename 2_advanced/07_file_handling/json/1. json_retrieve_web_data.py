
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


def new_data(data):
    today_date = datetime(int(data['year']), int(data['month']),
                          int(data['day'])).data('%Y-%m-%d')
    if today_date == today:
        return True
    return False
    

if __name__ == '__main__':
    print(today)
    status = return_status('https://xkcd.com/info.0.json')
    data = retrieve_data('https://xkcd.com/info.0.json')
    print(status, data)
    print(new_data(data))


