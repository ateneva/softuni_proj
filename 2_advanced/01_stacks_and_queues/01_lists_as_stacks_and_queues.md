  

![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f4d4.png?version=6.0.0) Lists as Stacks and Queues
============================================================================================================

  

![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f4d9.png?version=6.0.0) Stacks & Queues Lecture:
----------------------------------------------------------------------------------------------------------

*   **Doncho** 

> [_https://softuni.bg/trainings/resources/video/49835/video-18-may-2020-doncho-minkov-python-advanced-may-2020/2839_](https://softuni.bg/trainings/resources/video/49835/video-18-may-2020-doncho-minkov-python-advanced-may-2020/2839)

  

---

![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f5a5.png?version=6.0.0) Stacks & Queuse Exercises:
------------------------------------------------------------------------------------------------------------

*   **Tanya**



![](https://paper.dropboxstatic.com/static/img/ace/emoji/1f4cc.png?version=6.0.0) **Lists Revision**
----------------------------------------------------------------------------------------------------

 [_✓ Lecture 9: Lists Advanced_](https://app.asana.com/0/1133134368889333/1154519219101715/f)_;_

> [_https://www.geeksforgeeks.org/python-list/?ref=lbp#lm_](https://www.geeksforgeeks.org/python-list/?ref=lbp#lm)

  

dynamic **mutable data structure**

*   **can be extended** → [https://www.geeksforgeeks.org/python-list/?ref=lbp](https://www.geeksforgeeks.org/python-list/?ref=lbp)
    *  **l.insert** _(index, value)_
    *  **l.append** _(value)_
    *  **l.extend** _(any iterable)_ 

> _→ adds any iterable_ **_a_**_t the end of the list_


*   **can be shrunk:**
    *   **l.remove**_(value)_ 

> _→ removes the first occurence it finds_


*  **l.pop**_(\[index)_ 

> _→_ [_https://www.geeksforgeeks.org/python-list-pop_](https://www.geeksforgeeks.org/python-list-pop)

  

*   **del** l\[1\]

  

![](https://t4668229.p.clickup-attachments.com/t4668229/6697509e-fd10-44b2-8b06-dd46cfd643b4/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/44bc1987-a93c-4516-8a53-48f1feb7ba91/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/24f86a63-f74d-4eb0-8fd5-5b88516166e0/image.png)

  

```python
def reverse(numbers):
    #numbers = input().split(' ')
    stack = []

    for n in range(len(numbers)):
        stack.append(numbers.pop())

    print(' '.join(stack))

reverse(input().split(' '))
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/f5dfbe6f-d573-4104-bef6-47b83518ec6a/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/956173d8-0057-45bd-9dfa-6a9c27f83ac9/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/fd1b02ad-90a7-475a-92fb-651a41f66184/image.png)

  

![](https://t4668229.p.clickup-attachments.com/t4668229/85ff0f72-7c66-40bb-8a92-af172751ff68/image.png)

  

```python
from collections import deque
queue = deque()

while True:
    customer = input()

    if customer == 'End':
        print(f'{len(queue)} people remaining.')
        break

    elif customer == 'Paid':
        # print customers in queue
        while queue:
            print(queue.popleft())

    else:
        # print remaining people
        queue.append(customer)
```


* **count()** 

>  _This function_ **_counts the number of occurrences_** _of value mentioned in arguments._

  

### Adding Elements

*   **append()**

> _This function is used to_ **_insert_** _the value in its argument to the_ **_right end_** _of deque._


*   **appendleft()**

> _This function is used to_ **_insert_** _the value in its argument to the_ **_left end_** _of deque._


*   **insert(i, a)**

> _This function_ **_inserts the value_** _mentioned in arguments(a)_ **_at index(i)_** _specified in arguments._

  

*   **extend(iterable)** 

> _This function is used to_ **_add multiple values at the right end_** _of deque. The argument passed is an iterable._


*   **extendleft(iterable)** 

> _This function is used to_ **_add multiple values at the left end_** _of deque. The argument passed is an iterable._ **_Order is reversed_** _as a result of left appends._

  

![](https://paper.dropboxstatic.com/static/img/ace/emoji/274c.png?version=6.0.0) Removing Elements:

*   **pop()** 

> _This function is used to_ **_delete_** _an argument from the_ **_right end_** _of deque._

  

*   **popleft()** 

> _This function is used to_ **_delete_** _an argument from the_ **_left end_** _of deque._

  

*   **remove()** 

> _This function_ **_removes the first occurrence_** _of value mentioned in arguments_

  

[https://www.geeksforgeeks.org/deque-in-python/](https://www.geeksforgeeks.org/deque-in-python/)

  

```python
from collections import deque
q = deque()

q.append(1)
q.append(2)
q.append(3)

while q:
    print(q.popleft())

# manipulating the queue from left to right is also possible
# that's why deque stands for double-ended queeu
# however doing this is not ususally used

q.appendleft(1)
q.appendleft(2)
q.appendleft(3)

while q:
    print(q.pop())
```

  

![](https://t4668229.p.clickup-attachments.com/t4668229/970f7826-c1f4-429c-a333-1b9248f2aef6/image.png)

  

```python
from collections import deque
q = deque([1, 2, 3, 4, 5, 6, 7, 8])

print(q)
q.rotate(3)
print(q)
print(q.popleft())
print(q)

deque([1, 2, 3, 4, 5, 6, 7, 8])
deque([6, 7, 8, 1, 2, 3, 4, 5])
6
deque([7, 8, 1, 2, 3, 4, 5])
```


## Stacks and Queues problems: 

* [00_lists_as_stacks_and_queues.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/01_stacks_and_queues/01_00_lists_as_stacks_and_queues.py)
* [02_matching_brackets.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/01_stacks_and_queues/01_02_matching_brackets.py)
* [03_superket.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/01_stacks_and_queues/01_03_superket.py)
* [04_water_dispenser.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/01_stacks_and_queues/01_04_water_dispenser.py)
* [05_hot_potato.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/01_stacks_and_queues/01_05_hot_potato.py)
* [ex_01_stacks_reverse_numbers.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/01_stacks_and_queues/01_ex_01_stacks_reverse_numbers.py)
* [ex_02_stacks_maximum_and_minimum_element.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/01_stacks_and_queues/01_ex_02_stacks_maximum_and_minimum_element.py)
* [ex_03_queues_03_fast_food.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/01_stacks_and_queues/01_ex_03_queues_03_fast_food.py)
* [ex_04_stacks_fashion_boutique.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/01_stacks_and_queues/01_ex_04_stacks_fashion_boutique.py)


* [2020-06-07-01_bombs.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/exam_prep/2020-06-07-01_bombs.py)
* [2020-08-19-01_taxi_express.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/exam_prep/2020-08-19-01_taxi_express.py)
* [2020-12-16-01_problem_1.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/exam_prep/2020-12-16-01_problem_1.py)
* [2021-04-14-01_pizza_delivery.py](https://github.com/ateneva/softuni_proj/blob/main/2_advanced/exam_prep/2021-04-14-01_pizza_delivery.py)

Further Reading
===============