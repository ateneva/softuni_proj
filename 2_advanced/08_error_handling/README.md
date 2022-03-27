# Logging module

Logging provides a set of convenience functions for simple logging usage. 

These are:
* `debug()`   - detailed output of events that occur during normal operation of a program
* `info()`    - report events that occur during normal operation of a program
* `warning()` - if there is nothing the client application can do but note the event
* `error()`   - raise an exception
* `critical()`

```python
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```


```python
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
```


## Logging to a file

```python
import logging

logging.basicConfig(
    filename='example.log', 
    filemode='w', 
    encoding='utf-8',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
```

### displaying the date/time in messages

```python
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')
```

```
2010-12-12 11:41:42,612 is when this event was logged.
```

----------------------------
### `logging.info`

```python
import requests
import json
import logging

def call_api(hook, header, response_calls, date_range):
    data = []
    
    for r in response_calls:
        api_call = hook + r + date_range
        response = requests.get(api_call, headers=header)
        
        if response.status_code != 200:
            logging.info(f'Request failed: {response.status_code}: {response.content}')
        
        total_records = json.loads(response.content.decode('utf-8'))['total_records']
        response_call = (api_call, total_records)
        data.append(response_call)
    
    logging.info(f'responses: {data[0][1]}, non_responses: {data[1][1]}')
    return data
```


## References
* https://docs.python.org/3/howto/logging.html
* https://realpython.com/python-logging/
* 