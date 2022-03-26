
## Reading JSON from a file with `json` library

```python
import json

with open('json_data.json') as json_file:
    data = json.load(json_file)
    print(data)
```

```python
import json

python_dictionary = json.loads(json_string)
print(python_dictionary)
```

This one is especially useful for parsing REST API responses that send JSON. 
This data comes to you as a string, which you can then pass to `json.loads()` directly, 
and you have a much more manageable dictionary to work with!


## Writing JSON to a file with `json` library
```python
import json

data = {
    'employees' : [
        {
            'name' : 'John Doe',
            'department' : 'Marketing',
            'place' : 'Remote'
        },
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'Remote'
        },
        {
            'name' : 'Don Joe',
            'department' : 'Software Engineering',
            'place' : 'Office'
        }
    ]
}
json_string = json.dumps(data)
print(json_string)

# Directly from dictionary
with open('json_data.json', 'w') as outfile:
    json.dump(json_string, outfile)
  
# Using a JSON string
with open('json_data.json', 'w') as outfile:
    outfile.write(json_string)
```

### Pretty-Printing

```python
import json
data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
print(json.dumps(data, indent=4))
```

### Use `sort_keys=True` to enforce key order
```python
import json
data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
print(json.dumps(data, sort_keys=True, indent=4))
```

```json
{
    "people": [
        {
            "website": "stackabuse.com", 
            "from": "Nebraska", 
            "name": "Scott"
        }
    ]
}
```

### Automatically escape non-ASCII characters
```python
import json
data = {'item': 'Beer', 'cost':'£4.00'}
jstr = json.dumps(data, indent=4)
print(jstr)
```

```json
{
    "item": "Beer",
    "cost": "\u00a34.00"
}
```

```python
import json
data = {'item': 'Beer', 'cost':'£4.00'}
jstr = json.dumps(data, ensure_ascii=False, indent=4)
print(jstr)
```

```json
{
    "item": "Beer",
    "cost": "£4.00"
}
```


## Writing JSON to a file with `pandas` library

```python
from pandas import DataFrame

data = {'Product': ['Desktop Computer','Tablet','iPhone','Laptop'],
        'Price': [700,250,800,1200]
        }

df = DataFrame(data, columns= ['Product', 'Price'])

df.to_json (r'/Users/angelina.teneva/Downloads/export_dataFrame.json')
```

```json
{
  "Product": {
    "0": "Desktop Computer",
    "1": "Tablet",
    "2": "iPhone",
    "3": "Laptop"
  },
  "Price": {
    "0": 700,
    "1": 250,
    "2": 800,
    "3": 1200
  }
}
```

```python
df.to_json (r'/Users/angelina.teneva/Downloads/export_dataFrame.json', orient='index')
```

```json
{
  "0": {
    "Product": "Desktop Computer",
    "Price": 700
  },
  "1": {
    "Product": "Tablet",
    "Price": 250
  },
  "2": {
    "Product": "iPhone",
    "Price": 800
  },
  "3": {
    "Product": "Laptop",
    "Price": 1200
  }
}
```

# References
* https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
* https://realpython.com/python-json/

* https://datatofish.com/export-pandas-dataframe-json/
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html