![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f4a2.png?version=6.0.0) Comprehensions
================================================================================================

  

![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f4d9.png?version=6.0.0) Comprehensions Lecture:
---------------------------------------------------------------------------------------------------------

### **Doncho**:

> [_https://softuni.bg/trainings/resources/video/50236/video-01-june-2020-doncho-minkov-python-advanced-may-2020/2839_](https://softuni.bg/trainings/resources/video/50236/video-01-june-2020-doncho-minkov-python-advanced-may-2020/2839)

  

![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f5a5.png?version=6.0.0) Comprehensions Exercises:
-----------------------------------------------------------------------------------------------------------

### **Tanya**

> [_https://softuni.bg/trainings/resources/video/50268/video-02-june-2020-tanya-staneva-python-advanced-may-2020/2839_](https://softuni.bg/trainings/resources/video/50268/video-02-june-2020-tanya-staneva-python-advanced-may-2020/2839)

  

Comprehensions Notes: 
----------------------

1.  Loop over the collection in a list or dictionary
2.  Perform an operation on every element of that collection
3.  Collect the results in a new list or dictionary


![](https://t4668229.p.clickup-attachments.com/t4668229/14758d89-e911-41cb-877a-5562d2f3605c/image.png)


![](https://t4668229.p.clickup-attachments.com/t4668229/62754a32-7d36-4cb8-b914-6b475192fa9c/image.png)

  

```python
squares = [ i**2 for i in range(10) ]
squares3_dict = { i: i**2 for i in range(30) if i % 3 == 0 } 
result = sum([ i**2 for i in range(10) ]) 
new_wordlist = [new_word.strip().lower() for new_word in open('words.txt', 'r')] 
```

[✓ Chapter 2: Data Containers in Python](https://app.asana.com/0/1133134368889333/1133183033786985) 

[✓ Chapter 8: Structured Data](https://app.asana.com/0/1133134368889333/1133183033787022)

[✓ List Comprehensions and Lambda Functions](https://app.asana.com/0/1119380253334055/1161069642241615)

## **list comprehensions usage**

NB! comprehensions are **one idea slower** than loops but they add to **more readable code**

* transforming lists 

>  **_\[sq \*\* (1/2)_** _for sq in squares_**_\], \[l.upper()_** _for l in letters_**_\]_**

  

* reducing lists 

>  _\[i for i in int_ **_if i >=50_**_\], \[i for i in range(len(numbers))_ **_if numbers\[i\] % 2 == 0_**_\]_


![](https://t4668229.p.clickup-attachments.com/t4668229/7d3e7a07-aaf6-445f-92f3-587a48dea261/image.png)

  

```python
# 04. even numbers --> comprehension
numbers = list(map(int, input().split(', ')))  # map to integers and convert to a list
evens = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(evens)
```

  

```python
# 06. Group of 10s ------------------------------------------------------------------
numbers = list(map(int,input().split(", ")))
group = 10

while len(numbers) > 0:
    filtered = [num for num in numbers if num <= group]
    numbers = [num for num in numbers if num > group]
    print(f"Group of {group}'s: {filtered}")
    group += 10
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/54d70710-c080-408c-9c8b-b6e62a451d41/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/2341b716-7b21-4bd9-8c8b-8d3dfc11983e/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/897b3bfe-9d45-4fea-adc0-12edf39d81ee/image.png)

  

```python
# simple conditional statements
numbers = [int(n) for n in input().split(" ")]
evens = [e for e in numbers if e % 2 == 0]

# VS

# if-else statements
nums = [1, 2, 3, 4, 5, 6]
filtered = [True if x % 2 == 0 else False for x in nums]
```

  

```python
# you can evoke functions in comprehensions
def transform(number):
     return number ** 2

numbers = [1, 2, 3, 4, 5]
transformed_numbers = [transform(number) for number in numbers]
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/d702800e-e56c-4597-850b-1845a357d18f/image.png)

  

```python
# build a dicionary from a list
nums = [1, 2, 3]
cubes = {num:num ** 3 for num in nums}
print(cubes) 
# {1: 1, 2: 8, 3: 27}

# build a dictionary with the squares of even numbers
numbers = range(10)
even_squares= {n:n**2 for n in numbers if n % 2 == 0}
print(even_squares) 
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# build a dictionary from another dictionary
originals= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
doubled= {k:v*2 for (k,v) in originals.items()}
print(doubled)    
# {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/7cb5bbcc-e5a0-46b6-9dec-15cbf4fec580/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/9c1fb503-2a99-4771-b22a-07cb14274e9d/image.png)

  

```python
# nested comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
```


🆚

```python
# better real life solution
def generate_row(size):
    return [j for j in range(size)]

matrix = [generate_row(3) for _ in range(3)]
print(matrix)
```


![](https://t4668229.p.clickup-attachments.com/t4668229/0e19eec5-4e43-46c1-ae2f-010ccc2cfc43/image.png)

  

```python
def read_matrix():
    rows = int(input())
    matrix = []
    for r in range(rows):
        numbers = [int(n) for n in input().split(", ")]
        matrix.append(numbers)

    return matrix

sublists = read_matrix()
full_matrix = [sublist for sublist in sublists]
flattened_matrix =[s for sublist in sublists for s in sublist]

print(flattened_matrix)
```



* [01_ascii_values.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_01_ascii_values.py)
* [02_no_vowels.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_02_no_vowels.py)
* [03_even_matrix.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_03_even_matrix.py)
* [04_flatten_matrix.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_04_flatten_matrix.py)
* [05_filter_numbers.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_05_filter_numbers.py)


* [ex_01_word_filter.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_ex_01_word_filter.py)
* [ex_02_word_lengths.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_ex_02_word_lengths.py)
* [ex_03_capitals.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_ex_03_capitals.py)
* [ex_04_number_classification.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_ex_04_number_classification.py)
* [ex_07_flatten_lists.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_ex_07_flatten_lists.py)
* [ex_08_hero_inventory.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_ex_08_hero_inventory.py)
* [ex_09_bunkers.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/04_comprehensions/04_ex_09_bunkers.py)

  

Further Reading
===============