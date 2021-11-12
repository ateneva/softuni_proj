  

Lists
=======================================================================================

  

## Lists Basic Lecture:


### **Jordan = basics:**

> _Part 1:_ [_https://softuni.bg/trainings/resources/video/46165/video-28-january-2020-jordan-jambazov-part-1-python-fundamentals-january-2020/2603_](https://softuni.bg/trainings/resources/video/46165/video-28-january-2020-jordan-jambazov-part-1-python-fundamentals-january-2020/2603)

> _Part 2:_ [_https://softuni.bg/trainings/resources/video/46166/video-28-january-2020-jordan-jambazov-part-2-python-fundamentals-january-2020/2603_](https://softuni.bg/trainings/resources/video/46166/video-28-january-2020-jordan-jambazov-part-2-python-fundamentals-january-2020/2603)

  

### Lists Basic Exercises:

*   **Tanya** 

>  [_https://softuni.bg/trainings/resources/video/43259/video-04-october-2019-tanya-staneva-python-fundamentals-september-2019/2442_](https://softuni.bg/trainings/resources/video/43259/video-04-october-2019-tanya-staneva-python-fundamentals-september-2019/2442)

*   **Slavi** 

>  [_https://softuni.bg/trainings/resources/video/46216/video-30-january-2020-slavi-kapsalov-python-fundamentals-january-2020/2603_](https://softuni.bg/trainings/resources/video/46216/video-30-january-2020-slavi-kapsalov-python-fundamentals-january-2020/2603)
> 
> 1.  **ctrl + q** return the documentation of a function/method

Homework

1.  **1000 out of 1000** [https://judge.softuni.bg/Contests/Compete/Results/Simple/1725](https://judge.softuni.bg/Contests/Compete/Results/Simple/1725)

  

Lists Advanced Lecture:
---------------------------------------------------------------------------------------------------------

1.  **Doncho**
2.  **Jordan**

  

Lists Advanced Exercises:
-----------------------------------------------------------------------------------------------------------

1.  **Tanya**
2.  **Slavi**


*   **Lists Basic** \>>> [https://app.asana.com/0/1133134368889333/1154519219101711/f](https://app.asana.com/0/1133134368889333/1154519219101711/f) 
*   **Lists Advanced** >>> [https://app.asana.com/0/1133134368889333/1154519219101715/f](https://app.asana.com/0/1133134368889333/1154519219101715/f)

![](https://paper-attachments.dropbox.com/s_95A73BE24A04710EED7E4BB0277A696A1E68E54E6BA9A7750CBF8BEA09071651_1610273786119_image.png)

![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f4cc.png?version=6.0.0) Lists Basics:
-----------------------------------------------------------------------------------------------

1.  use the split function to **create a list from string** `list.**split**(", ")`
2.  **create a string** from a list `print(", ".join(my_list))`
3.  lists can be generated using the **"range"** function
4.  slicing and dicing using indices \[1\], **\[-1\]**


![](https://t4668229.p.clickup-attachments.com/t4668229/798928a2-1b9b-4d5f-b1aa-622e1d5dee98/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/6e7879ef-67a2-4cd2-8a8b-6b4204f2bc67/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/56924c4e-719a-47c8-aa3e-2eba16db4acc/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/56f70647-3221-42c0-924b-b59894ac590e/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/e6b071b1-9a69-4081-a4ec-fc1b0004ef6e/image.png)


```python
# 02. strange zoo ------------------------------
tail = input()
body = input()
head = input()

meerkat = [tail, body, head]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

animal = meerkat[::1]   # reverse the list

print(meerkat, animal)
```


![](https://t4668229.p.clickup-attachments.com/t4668229/e2f7202f-41ac-4e8d-b7f6-393c19bc92f6/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/2df42280-962d-4498-88bc-a537e22143ea/image.png)


![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f4cd.png?version=6.0.0) Creating Lists:
-------------------------------------------------------------------------------------------------

```python
import reader to create from file
mylist = []
mylist = list()
```

  

### Searching for elements within a list
1.  **in**
2.  **not in**

  

### Slicing lists
* from beginning (positive indexing) --> **first 3**  **[:3]**
* from the end (negative indexing) --> **last 3** **[-3:]**
* retrieving more than 1 element {slices) --> **[0:4] or [-3:], [:5]**
* list within a list --> **fb_data[1][-1]**
* reversing a list **--> fb_data[::-1]**

  

### Looping through lists:

1.  for loops
2.  while loops


![](https://t4668229.p.clickup-attachments.com/t4668229/a3b8aad7-e73c-4f84-b44c-3305af508842/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/411e6209-49b2-4a3b-8640-436f3acaf396/image.png)

  

### List Methods

> [https://www.w3schools.com/python/python\_ref\_list.asp](https://www.w3schools.com/python/python_ref_list.asp)

  

### Adding elements:

* `mylist.append(element)` -> add single element at the end
* `mylist.extend([iterable])` -> add **multiple elements** at the end
* `mylist.insert(index, element)` -> add a single element **at a specified index**

```python
# 01. courses ---------------------------------
n = int(input())
courses = []

for n in range(n):
    course = input()
    courses.append(course)
print(courses)
```


![](https://t4668229.p.clickup-attachments.com/t4668229/b6ce9ada-5194-43a0-83ec-809044b916e3/image.png)


### **Removing elements:**

*  `mylist.clear()` removes all elements

NB! if a list is simply re-assigned to a new one and not copied, **.clear()** clears both

  

* `mylist.pop(element)` - removes the **last element** or the **one at the specified position** and returns it

* `mylist.remove(element)` -  removes by **value first occurrence**


```python
# 04. search ------------------------------------------------------
n = int(input())
word = input()
phrases = []

for i in range(n):
    phrase = input()
    phrases.append(phrase)
print(phrases)

for i in range(len(phrases) - 1, -1, -1):
    selection = phrases[i]
    if word not in selection:
        phrases.remove(selection)
print(phrases)
```

![](https://t4668229.p.clickup-attachments.com/t4668229/d8de17bd-629c-4820-8dac-0509f33dd7d1/image.png)


### Other Key Methods

* `mylist.count(element)` -  **finds all occurrences in** a list
* `mylist.index(element)` -  finds the index **of the first occurrence**
* `mylist.reverse()` -  reverses the order of the elements in the list
* `mylist.sort(reverse = True)` -  **method** only applicable to list


![](https://t4668229.p.clickup-attachments.com/t4668229/ac0d30a1-a22f-4e1c-9c22-059bd79b7f89/image.png)

NB! There is also a function `mylist = sorted(mylist, reverse = True)` that is applicable **to any iterable**

* https://www.geeksforgeeks.org/list-methods-in-python-set-2-del-remove-sort-insert-pop-extend/

```python
# 02. Big Numbers Lover ------------------------------------------------------
numbers = input().split(" ")
biggest = "".join(sorted(numbers, reverse=True))

print(biggest)
```


| Method | Description |
| ---| --- |
| [append()](https://www.w3schools.com/python/ref_list_append.asp) | Adds an element at the end of the list |
| [clear()](https://www.w3schools.com/python/ref_list_clear.asp) | Removes all the elements from the list |
| [copy()](https://www.w3schools.com/python/ref_list_copy.asp) | Returns a copy of the list |
| [count()](https://www.w3schools.com/python/ref_list_count.asp) | Returns the number of elements with the specified value |
| [extend()](https://www.w3schools.com/python/ref_list_extend.asp) | Add the elements of a list (or any iterable), to the end of the current list |
| [index()](https://www.w3schools.com/python/ref_list_index.asp) | Returns the index of the first element with the specified value |
| [insert()](https://www.w3schools.com/python/ref_list_insert.asp) | Adds an element at the specified position |
| [pop()](https://www.w3schools.com/python/ref_list_pop.asp) | Removes the element at the specified position |
| [remove()](https://www.w3schools.com/python/ref_list_remove.asp) | Removes the first item with the specified value |
| [reverse()](https://www.w3schools.com/python/ref_list_reverse.asp) | Reverses the order of the list |
| [sort()](https://www.w3schools.com/python/ref_list_sort.asp) | Sorts the list |

  

![](https://t4668229.p.clickup-attachments.com/t4668229/4030189c-a092-4f26-af23-dfc565388b25/image.png)

  

```python
# 03.palindrome strings ------------------------------------------------------------
words = input().split(" ")
searched = input()
palindromes = []
for word in words:
    if word == "".join(reversed(word)): # another way to reverse is word[::-1]
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(searched)} times")
```



More Advanced List Methods: 
----------------------------------------------------------------------------------------------------------------------------------

1.  anonymous functions are ones **that is not explicitly defined**

* `lambda x: int(x)`

> **_1-line_** **_temporary_** _function to be passed as an argument in other functions_


![](https://t4668229.p.clickup-attachments.com/t4668229/2db5cab4-ef61-4161-955f-5972b6a5e852/image.png)


* `map(function, iterable)` - apply a function on each of the elements in a list
    * NB! **_comprehensions are preferred over map_** 

```python
# use map method to convert a list of strings to a list of integers
list(map(lambda x: int(x), mylist))
```


![](https://t4668229.p.clickup-attachments.com/t4668229/7645cb0e-91b5-400c-8003-b9de9e3df4da/image.png)


```python
# 04.even numbers -------------------------
numbers = list(map(int,input().split(', ')))  # map to integers and convert to a list
indices_for = []

for i in range(len(numbers)):
    number = numbers[i]
    if number % 2 == 0:
        indices_for.append(i)
print(indices_for)
```


* `filter**(function, iterable)`

>  _filter the elements of a list through a condition defined in a function_  
> **_comprehensions are preferred over filter_**


```python
# use filter method to return all instances that fulfill a condition
list(filter(lambda x: x % 2 ==0), mylist)
```

![](https://t4668229.p.clickup-attachments.com/t4668229/58c567f4-4377-4ba8-aae7-d21cb71d93f4/image.png)


```python
# approach 2 --> lambda, map and filter methods
employees = input().split(" ")
improvement_factor = int(input())

happiness = list(map(lambda e: int(e) * improvement_factor, employees))
employees_count = len(happiness)

happy = len(list(filter(lambda e: e >= (sum(happiness) / employees_count), happiness)))  # count happy people
#print(happiness, employees_count, happy)

if happy >= employees_count / 2:
    print(f"Score: {happy}/{employees_count}. Employees are happy!")
else:
    print(f"Score: {happy}/{employees_count}. Employees are not happy!")
```


![](https://t4668229.p.clickup-attachments.com/t4668229/e6a783be-1341-4cda-be5e-554040768685/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/5917406d-76f6-4790-9db0-da6a1d301e4d/image.png)



## List problems: 
  

* [07_easter_gifts.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/01_lists/01_lists_07_easter_gifts.py)
* [08_seize_the_fire.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/01_lists/01_lists_08_seize_the_fire.py)
* [09_hello_france.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/01_lists/01_lists_09_hello_france.py)
* [10_bread_factory.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/01_lists/01_lists_10_bread_factory.py)


### 2019-03-10

* [group1_02_hello_france.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-03-10/group1_02_hello_france.py)
* [group1_03_last_stop.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-03-10/group1_03_last_stop.py)
* [group2_02_seize_the_fire.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-03-10/group2_02_seize_the_fire.py)
* [group2_03_the_final_quest.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-03-10/group2_03_the_final_quest.py)


### 2019-04-16

* [02_easter_gifts.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-04-16/02_easter_gifts.py)
* [03_easter_shopping.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-04-16/03_easter_shopping.py)

  

### 2019-06-30

* [group1_02_number_array.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-06-30/group1_02_number_array.py)
* [group1_03_contact_list.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-06-30/group1_03_contact_list.py)
* [group2_02_tasks_planner.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-06-30/group2_02_tasks_planner.py)
* [group2_03_froggy_squad.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-06-30/group2_03_froggy_squad.py)


### 2019-08-06

* [02_treasure_hunt.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-08-06/02_treasure_hunt.py)
* [03_man_o_war.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-08-06/03_man_o_war.py)


### 2019-11-02

* [group1_02_weaponsmith.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-11-02/group1_02_weaponsmith.py)
* [group1_03_wizard_poker.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-11-02/group1_03_wizard_poker.py)
* [group2_02_friendlist_maintenance.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-11-02/group2_02_friendlist_maintenance.py)
* [group2_03_tanks_collector.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-11-02/group2_03_tanks_collector.py)


### 2019-12-10

* [02_archery_tournament.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-12-10/02_archery_tournament.py)
* [03_school_library.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2019-12-10/03_school_library.py)

### 2020-02-29

* [group1_02_muonline.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2020-02-29/group1_02_muonline.py)
* [group1_03_inventory.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2020-02-29/group1_03_inventory.py)
* [group2_02_shopping_list.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2020-02-29/group2_02_shopping_list.py)
* [group2_03_heart_delivery.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2020-02-29/group2_03_heart_delivery.py)


### 2020-04-07

* [02_shoot_for_the_win.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2020-04-07/02_shoot_for_the_win.py)
* [03_moving_target.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2020-04-07/03_moving_target.py)


### 2020-07-05

* [02_array_modifier.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2020-07-05/02_array_modifier.py)
* [03_numbers.py](https://github.com/ateneva/softuni_proj/blob/main/1_fund/mid%20exam%20preparation/2020-07-05/03_numbers.py)


Further Reading
===============