import requests
import json

response = requests.get('https://api.covid19india.org/state_district_wise.json')
print(response.status_code)
print(response.content)

