
## Labs:


### **Doncho:** 

> [_https://softuni.bg/trainings/resources/video/49924/video-21-may-2020-doncho-minkov-python-advanced-may-2020/2839_](https://softuni.bg/trainings/resources/video/49924/video-21-may-2020-doncho-minkov-python-advanced-may-2020/2839)



### **Tanya:**

> [_https://softuni.bg/trainings/resources/video/49934/video-22-may-2020-tanya-staneva-python-advanced-may-2020/2839_](https://softuni.bg/trainings/resources/video/49934/video-22-may-2020-tanya-staneva-python-advanced-may-2020/2839)

### Tuples: 
* sequences of **immutable** objects

```python
# creating a tuple 
t = (1,2,3)
print(t[0])

# creating a tuple with a single element
t = (1, )
```

### Tuple Methods
There are only 2 tuple methods

| Method | Description |
| ---| --- |
| [count()](https://www.w3schools.com/python/ref_tuple_count.asp) | Returns the number of times a specified value occurs in a tuple |
| [index()](https://www.w3schools.com/python/ref_tuple_index.asp) | Searches the tuple for a specified value and returns the position of where it was found |

```python
numbers = (1,2,1,3,1)
numbers.count(1) # 3
```

```python
names = ("Pesho", "Gosho", "Gosho")
names.index("Gosho") # 1
```

**Problem: Count same values**
* _You will be given floating point numbers separated by a space_
* _Count the occurences of each value and print it_

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


### Tuple unpacking
* Tuple unpacking extracts the tuple elements and assigns them

```python
data = (1,2,3)
x, y, z = data

print(x)  # 1
print(y)  # 2
print(z)  # 3
```

### the SET method
* You can use the set method to extract only unique elements from a list
* the **SET** method returns a set with UNIQUE values

```python
numbers = [1,2,2,3,1,4,5,4]
unique_numbers = list(set(numbers)) # [1,2,3,4,5
```

### SET
* unordered collection of items
* each set element is unique
* SETS are **mutable**, so we can add or remove elements
  
### Set Operators
```python
a = set([1,2,3,4])
b = set([3,4,5,6])

print(a - b)  # find members that are in a but not in b
print(a | b)  # find the members that are in either a or b
print(a ^ b)  # find the members that are not in both
print(a & b)  # find the members that are in both
```

### Set Methods
```python
a = set([1,2,3,4])
b = set([3,4,5,6])

print(a.union(b))                 # equivalent to a | b
print(a.intersection(b))          # equivalent to a & b
print(a.issubset(b))              # equivalent to a <= b
print(a.issuperset(b))            # equivalent to a >= b
print(a.difference(b))            # equivalent to a - b
print(a.symmetric_difference(b))  # equivalent to a ^ b
```

**Problem: Unique Names**
* You will be given a list and you have to print unique items
  * the order does not matter

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

Further Reading
===============

Sets in Python – Real Python

In this tutorial you'll learn how to work effectively with Python's set data type. You'll see how to define set objects in Python and discover the operations that they support and by the end of the tutorial you'll have a good feel for when a set is an appropriate choice in your own programs.

https://realpython.com/python-sets/

