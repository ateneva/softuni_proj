# Dictionaries


> LinkedIn: Data Analysis in Python [✓ Chapter 2: Data Containers in Python](https://app.asana.com/0/1133134368889333/1133183033786985)   
> LinkedIn: Python Essential Training [✓ Chapter 8: Structured Data](https://app.asana.com/0/1133134368889333/1133183033787022)   
> DataQuest [✓ Dictionaries and Frequency Tables](https://app.asana.com/0/1133134368889333/1161069642241597)


## Dictionaries Lecture:

### **Doncho**

> [_https://softuni.bg/trainings/resources/video/44300/video-06-november-2019-doncho-minkov-python-fundamentals-september-2019/2442_](https://softuni.bg/trainings/resources/video/44300/video-06-november-2019-doncho-minkov-python-fundamentals-september-2019/2442)

* dictionary keys and values can be written into a list


```python
print(list(dd.keys()))
print(list(dd.values()))
```


* dictionary comprehensions

```buildoutcfg
{values[i]: int(values[i+1]) for i in range(0, n, 2)}
```
    * prior **python 3.6 dictionary keys do not have a fixed order**  
    * subsequent versions order dictionaries at the order of insertion

  

### Jordan

> https://softuni.bg/trainings/resources/video/47274/video-04-march-2020-jordan-jambazov-python-fundamentals-january-2020/2603

  

## Dictionaries Exercises:

### Tanya
### Slavi

* [_https://softuni.bg/trainings/resources/video/44375/video-08-november-2019-slavi-kapsalov-python-fundamentals-september-2019/2442_](https://softuni.bg/trainings/resources/video/44375/video-08-november-2019-slavi-kapsalov-python-fundamentals-september-2019/2442) 
> [_https://softuni.bg/trainings/resources/video/47339/video-05-march-2020-slavi-kapsalov-python-fundamentals-january-2020/2603_](https://softuni.bg/trainings/resources/video/47339/video-05-march-2020-slavi-kapsalov-python-fundamentals-january-2020/2603)
  

* dictionaries with data of different types(e.g. strings, integers) **can not be sorted**


```python
my_dict = {2: 'apple', 1: 'ball', 6: '7087'}

# reverse will apply to both elements
print(sorted(my_dict.items(), key=lambda x: (x[1], x[0]), reverse=True))  

# order descending by value, ascending by key
key_materials = dict(sorted(key_materials.items(), key=lambda el: (-el[1], el[0])))

dict = sorted(myDict.items(), key=lambda e: e[1][2])  # sort by key and value
courses = dict(sorted(courses.items(), key=lambda x: x[0]))  # sort by key
```



![](https://t4668229.p.clickup-attachments.com/t4668229/5d4b107d-9ca3-422a-96c4-cc5c3076292a/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/38e1a3ed-f81f-46a4-9ab5-3b70e5623fa7/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/347d4606-e08b-41cb-a2b7-8a6f96173e62/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/970ee82b-1f6a-4314-ab26-59c286a0719a/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/e213d35b-fd2a-47c8-adcf-2afc89c806c9/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/ae29b37f-f6eb-42bd-a572-03a3c120ad85/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/0aa1474c-3885-4ce6-aedc-678800a10f0a/image.png)

  

```python
# iterate through the keys to get the values
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    print(squares[key], end=" ")

# iterate through the keys to change the values
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    squares[key] *= 2

print(squares)
# {1: 2, 2: 8, 3: 18}

# iterate through the values to get the values
squares = {1: 1, 2: 4, 3: 9}
for value in squares.values():
    print(value, end=" ")

# iterate through key value pairs
squares = {1: 1, 2: 4, 3: 9}
for (key, value) in squares.items():
    print(f"Key: {key}, Value: {value}")  # returns a tuple 
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/596b1cc2-087b-4e03-81ce-4a5b2075b473/image.png)

  

```python
# check fro existence by looping through the whole dictionary
my_dict = {'name': 'Peter', 'age': 22}
if 'name' in my_dict:
    print(my_dict['name']) # Peter

# check for existence by looping through the keys
my_dict = {'name': 'Peter', 'age': 22}
if 'name' in my_dict.keys():
    print(my_dict['name']) # Peter

# check for existence by looping through the values
# not adviseable but possible
my_dict = {'name': 'Peter', 'age': 22}
if 22 in my_dict.values():
    print(my_dict['name'], my_dict['age']) 
```

  

Dictionary Methods
---------------------------------------------------------------------------------------------------

https://www.w3schools.com/python/python_ref_dictionary.asp

```python
capitals = {'Netherlands': 'Amsterdam', 'United Kingdom': 'London', 'France': 'Paris'}

# iterate through the dictionary
for capital in capitals:
    print(f'{capital} -> {capitals[capital]}')

# iterate through the keys
for key in capitals.keys():
    value = capitals[key]
    print(f'{key} -> {value}')

# iterate through the values
for value in capitals.values():
    print(value)

# iterate through the key-value pairs
for (key, value) in capitals.items():
    print(f'{key} -> {value}')

morecapitals = {'Hungary': 'Budapest', 'Lithuania': 'Vilnius'}
```

*   capitals.**clear** - removes all itemsin the existing dictionary object(s)

*   capitals.**copy** - copy creates a new object id

*   capitals.**pop**(key) - removes the last key

*   capitals.**popitem**() - removes the last inserted item

*   **del** capitals\[**key**\]

*   capitals.**update(**morecapitals**)** - add items from another dictionary


```python
# create a new identical dicionary
new_capitals = capitals.copy()
capitals.clear()
print(new_capitals, capitals)

# remove a specific item by pointing to its key
new_capitals.pop('United Kingdom')
print(new_capitals)

# add more items
new_capitals.update(morecapitals)
print(new_capitals)

# remove last inserted item
new_capitals.popitem()
print(new_capitals)
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/0a4a0bfd-dd6d-4e53-b2a6-82d69cde9bd9/image.png)

  

| Method | Description |
| ---| --- |
| [clear()](https://www.w3schools.com/python/ref_dictionary_clear.asp) | Removes all the elements from the dictionary |
| [copy()](https://www.w3schools.com/python/ref_dictionary_copy.asp) | Returns a copy of the dictionary |
| [fromkeys()](https://www.w3schools.com/python/ref_dictionary_fromkeys.asp) | Returns a dictionary with the specified keys and value |
| [get()](https://www.w3schools.com/python/ref_dictionary_get.asp) | Returns the value of the specified key |
| [items()](https://www.w3schools.com/python/ref_dictionary_items.asp) | Returns a list containing a tuple for each key value pair |
| [keys()](https://www.w3schools.com/python/ref_dictionary_keys.asp) | Returns a list containing the dictionary's keys |
| [pop()](https://www.w3schools.com/python/ref_dictionary_pop.asp) | Removes the element with the specified key |
| [popitem()](https://www.w3schools.com/python/ref_dictionary_popitem.asp) | Removes the last inserted key-value pair |
| [setdefault()](https://www.w3schools.com/python/ref_dictionary_setdefault.asp) | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| [update()](https://www.w3schools.com/python/ref_dictionary_update.asp) | Updates the dictionary with the specified key-value pairs |
| [values()](https://www.w3schools.com/python/ref_dictionary_values.asp) | Returns a list of all the values in the dictionary |


*  dictionary comprehensions

```python
avg_grades = {k: sum(v)/len(v) for k, v in students.items() if sum(v)/len(v) >= 4.50 }
```
  
## Dictionary problems:

* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_01\_bakery.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_01_bakery.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_02\_stock.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_02_stock.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_03\_statistics.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_03_statistics.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_04\_odd\_occurences.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_04_odd_occurences.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_05\_word\_synonyms.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_05_word_synonyms.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_11\_feed\_the\_animals.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_11_feed_the_animals.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_12\_on\_the\_way\_to\_anapurna.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_12_on_the_way_to_anapurna.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_13\_practice\_sessions.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_13_practice_sessions.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_ex\_01\_count\_chars\_in\_string.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_ex_01_count_chars_in_string.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_ex\_02\_a\_miners\_task.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_ex_02_a_miners_task.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_ex\_03\_legendary\_farming.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_ex_03_legendary_farming.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_ex\_04\_orders.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_ex_04_orders.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_ex\_05\_softuni\_parking.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_ex_05_softuni_parking.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_ex\_06\_courses.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_ex_06_courses.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_ex\_07\_student\_academy.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_ex_07_student_academy.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_ex\_08\_company\_users.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_ex_08_company_users.py)
* [https://github.com/ateneva/softuni\_proj/blob/main/1\_fund/02\_dictionaries/02\_dictionaries\_ex\_10\_softuni\_exam\_results.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/02_dictionaries/02_dictionaries_ex_10_softuni_exam_results.py)


Further Reading
===============