
# ******************************************* Lab ******************************

# 01.trains --------------------------------------------------------------
wagons = int(input())
train = [0] * wagons  # create a list with variable number of elements
command = input()

while command != 'End':
    do = command.split(' ')[0]
    people = list(map(lambda x: int(x), command.split(' ')[1:]))
    #print(do, people)

    if do == 'add':
        person = people[0]
        train[-1] += person   # ensures the 0s are replaced

    elif do == 'insert':
        position = people[0]
        person = people[1]

        if position == 0:     # ensures the 0s are replaced
            train[position] += person
        else:
            del train[position]
            train.insert(position, person)

    elif do == 'leave':
        position = people[0]
        person = people[1]
        left = train.pop(position)
        train.insert(position, left-person)

    command = input()
print(train)

# 02.ToDoList --------------------------------------------------------
td = input()
tasklist = [0] * 10

while td != 'End':
    items = td.split('-')
    importance = int(items[0])
    task = items[1]
    tasklist[importance-1] = task
    #tasklist.insert(importance, task)
    #print(tasklist)

    td = input()

prioritized = []
for t in tasklist:
    if t != 0:
        prioritized.append(t)
print(prioritized)

# 03.palindrome strings --------------------------------------------------------
words = input().split(" ")
searched = input()
palindromes = []
times_found = 0

for word in words:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(palindromes)
if searched in palindromes:
    for p in palindromes:
        if p == searched:
            times_found += 1
    #print(searched, times_found)
print(f"Found palindrome {times_found} times")

# OR you can use .count method to count specific items from a list
words = input().split(" ")
searched = input()
palindromes = []

for word in words:
    if word == "".join(reversed(word)): # another way to reverse is word[::-1]
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(searched)} times")

# 04.even numbers --------------------------------------------------------------

# approach 1 --> comprehension
numbers = list(map(int, input().split(', ')))  # map to integers and convert to a list
evens = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(evens)

# approach 2 -->  loop + append to empty list
numbers = list(map(int,input().split(', ')))  # map to integers and convert to a list
indices_for = []

for i in range(len(numbers)):
    number = numbers[i]
    if number % 2 == 0:
        indices_for.append(i)
print(indices_for)

# approach 3 --> define a function + use list and filter functions to retrieve the list
numbers = list(map(int,input().split(', ')))  # map to integers and convert to a list

def is_even(i):
    return numbers[i] % 2 == 0

indices_for = list(filter(is_even, range(len(numbers))))
print(indices_for)


# 05. the office ---------------------------------------------------------------

# approach 1 --> functions and comprehensions
happiness = list(map(int,input().split(' ')))                        # map to integers and convert to a list
improvement_factor = int(input())

happiness_index = [h * improvement_factor for h in happiness]        # calculate ind, happiness
employees_count = len(happiness_index)

def avg_happiness():
    return sum(happiness_index) / employees_count                    # calculate average happiness

happy = len([p for p in happiness_index if p >= avg_happiness()])    # count happy people

if happy >= employees_count / 2:
    print(f"Score: {happy}/{employees_count}. Employees are happy!")
else:
    print(f"Score: {happy}/{employees_count}. Employees are not happy!")


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


# *****************************Exercises ***************************************

# 01. which are in ----------------------------------------------------
# approach 1 --> nested loop
substrings = input().split(", ")
strings = input().split(", ")
result = []

#print(substrings, strings)
for substring in substrings:
    for string in strings:
        if substring in string \
                and substring not in result:
            result.append(substring)
print(result)

# approach 2 --> comprehension
substrings = input().split(", ")
strings = input()

#print(substrings, strings)
result = [substring for substring in substrings if substring in strings]
print(result)

# 02. Big Numbers Lover ------------------------------------------------------
numbers = input().split(" ")
biggest = "".join(sorted(numbers, reverse=True))

print(biggest)

# 03. Next Version -----------------------------------------------------------
# my solution
version = list(map(int, input().split(".")))
major = version[0]
incremental = version[1]
minor = version[2]

if minor == 9:
    version.remove(minor)
    version.remove(incremental)
    if incremental < 9:
        incremental += 1
        minor = 0
        version.extend([incremental, minor])
    else:
        version.remove(major)
        major += 1
        incremental = 0
        version.extend([major, incremental])
        version.insert(2, 0) # index, value to insert
else:
    minor = version.pop()
    minor += 1
    version.append(minor)

update = ".".join(map(str, version))
print(update)

# exercise solution
version = "".join(input().split("."))
update = ".".join(str(int(version) + 1))
print(update)

# 04. Office Chairs ------------------------------------------------------------
rooms = int(input())
free_chairs = []
total_free = 0

for room in range(1, rooms + 1):
    capacity = input().split(" ")
    occupied = int(capacity[1])
    free = len(capacity[0]) - occupied

    #print(capacity, occupied, free, sum(free_chairs))
    if free < 0:
        free_chairs.append(free)
        print(f'{abs(free)} more chairs needed in room {room}')
    else:
        free_chairs.append(free)

total_free = sum(free_chairs)
if total_free >= 0:
    print(f"Game On, {total_free} free chairs left")

# 05. Electron Distribution ----------------------------------------------------
electrons = int(input())
shells = []
shell_idx = 1

while electrons > 0:
    max_electrons = 2 * shell_idx ** 2
    if max_electrons > electrons:
        shells.append(electrons)
    else:
        shells.append(max_electrons)
    electrons -= max_electrons
    shell_idx += 1

print(shells)

# 06. Group of 10s -------------------------------------------------------------
numbers = list(map(int,input().split(", ")))
group = 10

while len(numbers) > 0:
    filtered = [num for num in numbers if num <= group]
    numbers = [num for num in numbers if num > group]
    print(f"Group of {group}'s: {filtered}")
    group += 10

# 07. Decipher This! -----------------------------------------------------------
words = input().split(" ")
# print(phrase)

for word in words:
    decoded = ''
    first_ascii = [ch for ch in word if ch.isdigit()]
    # left = [ch for ch in word if ch.isalpha()]

    left = list(word[len(first_ascii):])
    left[0], left[-1] = left[-1], left[0]  # NB! only works for lists, not for strings

    first = chr(int("".join(first_ascii)))
    rest = "".join(left)
    decoded += (first + rest)
    # print(first_ascii, first, left, decoded)
    print(decoded, end=" ")
