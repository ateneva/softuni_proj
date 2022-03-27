
### Making a request

```python
import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)

response.content()      # Return the raw bytes of the data payload
response.text()         # Return a string representation of the data payload
response.json()         # This method is convenient when the API returns JSON
```

### Handling query parameters

```python
import requests
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())
```

### Authenticating with a REST API

* with username and password
```python
import requests
from requests.auth import HTTPBasicAuth

requests.get(
  'https://api.github.com/user', 
  auth=HTTPBasicAuth('username', 'password')
)
```

* with an access token
```python
import requests
my_headers = {'Authorization' : 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)
```

### References
* https://www.nylas.com/blog/use-python-requests-module-rest-apis/#:~:text=There%20are%20a%20few%20common,and%20password%20into%20a%20website.
* https://www.geeksforgeeks.org/authentication-using-python-requests/?ref=lbp
* https://www.realpythonproject.com/how-to-authenticate-using-keys-basicauth-oauth-in-python/

### APIs
* https://docs.github.com/en/rest
* https://docs.genius.com/