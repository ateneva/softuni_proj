![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f587.png?version=6.0.0) Tuples and Sets
=================================================================================================

  

![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f4d9.png?version=6.0.0) Tuples & Sets Lecture:
--------------------------------------------------------------------------------------------------------

### **Doncho:** 

> [_https://softuni.bg/trainings/resources/video/49924/video-21-may-2020-doncho-minkov-python-advanced-may-2020/2839_](https://softuni.bg/trainings/resources/video/49924/video-21-may-2020-doncho-minkov-python-advanced-may-2020/2839)

  

![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f5a5.png?version=6.0.0) Tuples & Sets Exercises:
----------------------------------------------------------------------------------------------------------

### **Tanya:**

> [_https://softuni.bg/trainings/resources/video/49934/video-22-may-2020-tanya-staneva-python-advanced-may-2020/2839_](https://softuni.bg/trainings/resources/video/49934/video-22-may-2020-tanya-staneva-python-advanced-may-2020/2839)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/cc6b2e1d-5dda-48b8-8f75-c58324eb7052/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/fcb9b8cc-2f5e-4c96-bfe8-bef97b18ad0c/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/2e9ec6a2-1fdc-461a-a856-a25874bc9993/image.png)

  

| Method | Description |
| ---| --- |
| [count()](https://www.w3schools.com/python/ref_tuple_count.asp) | Returns the number of times a specified value occurs in a tuple |
| [index()](https://www.w3schools.com/python/ref_tuple_index.asp) | Searches the tuple for a specified value and returns the position of where it was found |

  

![](https://t4668229.p.clickup-attachments.com/t4668229/d01be009-21c9-43bc-9d77-4ad6c5fb518d/image.png)

  

```python
# count the same values
sequence = tuple([float(s) for s in input().split(" ")])
occurences = {}

for s in sequence:
    if s not in occurences:
        occurences[s] = 0
    occurences[s] += 1

for k, v in occurences.items():
    print(f'{k} - {v} times')
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/bcdb6cc1-b48a-4cb1-9ce1-b69b6d9a16a6/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/a3690f83-f814-4f85-be2e-d5d1fadd01ca/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/d277024c-8beb-46ee-8ee4-ae03ea883b6d/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/f1d90ed0-418e-4baa-b1e3-bd7cb8c9e16b/image.png)

  

```python
a = set("We're gonna need a bigger boat.")
b = set("I'm sorry, Dave. I'm afraid I can't do that.")

print_set(a - b)  # find members that are in a but not in b
print_set(a | b)  # find the members that are in either a or b
print_set(a ^ b)  # find the members that are not in both
print_set(a & b)  # find the members that are in both
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/5e552ada-28f6-4a4e-adc3-c80e3ff46d72/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/400044da-e7e7-42b0-a4df-cc056a08b1db/image.png)

  

  

![](https://t4668229.p.clickup-attachments.com/t4668229/3e751892-e9e2-43cf-aa34-4e212d864acf/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/37ef9580-309e-4ef7-aa64-4498c08289fa/image.png)

  

  

![](https://t4668229.p.clickup-attachments.com/t4668229/3e2aa8b2-b8c0-4e82-90a5-d0dd3a0a78f0/image.png)

  

```python
# create a non-empty set
n = int(input())
names = {input() for _ in range(n)}
[print(name) for name in names]

# approach 2 ->  create an empty set and add values to it
n = int(input())
unique_names = set()

for i in range(n):
    unique_names.add(input())

for person in unique_names:
    print(person)
```

  

Set Methods 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[https://www.w3schools.com/python/python\_ref\_set.asp](https://www.w3schools.com/python/python_ref_set.asp)

| [add()](https://www.w3schools.com/python/ref_set_add.asp) | Adds an element to the set |
| ---| --- |
| [clear()](https://www.w3schools.com/python/ref_set_clear.asp) | Removes all the elements from the set |
| [copy()](https://www.w3schools.com/python/ref_set_copy.asp) | Returns a copy of the set |
| [difference()](https://www.w3schools.com/python/ref_set_difference.asp) | Returns a set containing the difference between two or more sets |
| [difference\_update()](https://www.w3schools.com/python/ref_set_difference_update.asp) | Removes the items in this set that are also included in another, specified set |
| [discard()](https://www.w3schools.com/python/ref_set_discard.asp) | Remove the specified item |
| [intersection()](https://www.w3schools.com/python/ref_set_intersection.asp) | Returns a set, that is the intersection of two other sets |
| [intersection\_update()](https://www.w3schools.com/python/ref_set_intersection_update.asp) | Removes the items in this set that are not present in other, specified set(s) |
| [isdisjoint()](https://www.w3schools.com/python/ref_set_isdisjoint.asp) | Returns whether two sets have a intersection or not |
| [issubset()](https://www.w3schools.com/python/ref_set_issubset.asp) | Returns whether another set contains this set or not |
| [issuperset()](https://www.w3schools.com/python/ref_set_issuperset.asp) | Returns whether this set contains another set or not |
| [pop()](https://www.w3schools.com/python/ref_set_pop.asp) | Removes an element from the set |
| [remove()](https://www.w3schools.com/python/ref_set_remove.asp) | Removes the specified element |
| [symmetric\_difference()](https://www.w3schools.com/python/ref_set_symmetric_difference.asp) | Returns a set with the symmetric differences of two sets |
| [symmetric\_difference\_update()](https://www.w3schools.com/python/ref_set_symmetric_difference_update.asp) | inserts the symmetric differences from this set and another |
| [union()](https://www.w3schools.com/python/ref_set_union.asp) | Return a set containing the union of sets |
| [update()](https://www.w3schools.com/python/ref_set_update.asp) | Update the set with the union of this set and others |


![](https://t4668229.p.clickup-attachments.com/t4668229/bed2f9cb-d87c-4115-884c-0eb568118232/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/0ce7b941-e66c-43b5-b5cd-eed3fe4ec259/image.png)

  

```python
num_cars = int(input())
parking = set()

for c in range(1, num_cars + 1):
    # car = input().split(", ")
    # direction = car[0]
    # car_plate = car[1]
    (direction, car_plate) = input().split(", ")
  
    if direction == 'IN':
        parking.add(car_plate)
    else:
        parking.remove(car_plate)

if len(parking) > 0:
    [print(p) for p in parking]
else:
    print("Parking Lot is Empty")
```

## Tuples and sets problems

* [01_tuples_count_the_same_values.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_01_tuples_count_the_same_values.py)
* [02_tuples_average_student_grades.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_02_tuples_average_student_grades.py)
* [03_sets_record_unique_names.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_03_sets_record_unique_names.py)
* [04_sets_parking_lot.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_04_sets_parking_lot.py)
* [05_sets_softuni_party.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_05_sets_softuni_party.py)


* [ex_01_unique_usernames.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_ex_01_unique_usernames.py)
* [ex_02_sets_of_elements.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_ex_02_sets_of_elements.py)
* [ex_03_periodic_table.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_ex_03_periodic_table.py)
* [ex_04_count_symbols.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_ex_04_count_symbols.py)
* [ex_05_phonebook.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_ex_05_phonebook.py)
* [ex_06_longest_intersection.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_ex_06_longest_intersection.py)
* [ex_07_battle_of_names.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/02_tuples_and_sets/02_ex_07_battle_of_names.py)



Further Reading
===============


Sets in Python – Real Python

In this tutorial you'll learn how to work effectively with Python's set data type. You'll see how to define set objects in Python and discover the operations that they support and by the end of the tutorial you'll have a good feel for when a set is an appropriate choice in your own programs.

https://realpython.com/python-sets/

