
# ******************************************* Lab ****************************************************

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

# 03.palindrome strings ------------------------------------------------------------
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

# 04.even numbers ---------------------------------------------------------------------------

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


# 05. the office ------------------------------------------------------------------------------------------------

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


# ******************************************* Exercises ************************

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

# 08. Feed the Animals (exam problem)-------------------------------------------
# --------------70 points ------------------------------------------
def print_dict(dictionary, template):
    for (key, value) in dictionary.items():
        print(template.format(key, value))

info = input()
animals = {}
areas = {}

while info != 'Last Info':
    info = info.split(':')
    activity = info[0]
    animal = info[1]

    if activity == 'Add':
        food_limit = int(info[2])
        area = info[3]

        if animal not in animals:
            animals[animal] = food_limit
        else:
            animals[animal] += food_limit

        if area not in areas:
            areas[area] = [animal]
        else:
            if animal not in areas[area]:
                areas[area].append(animal)

    elif activity == 'Feed':
        food = int(info[2])
        area = info[3]

        if animal in animals:
            animals[animal] -= food
            if animals[animal] <= 0:
                animals.pop(animal)
                areas[area].remove(animal)
                print(f"{animal} was successfully fed")

    info = input()

# print(animals, areas)
# sort descending by value and ascending by key
animals = dict(sorted(animals.items(), key=lambda x: (-x[1], x[0])))
areas = dict(sorted(areas.items(), key=lambda a: -len(areas)))

print('Animals:')
print_dict(animals, '{} -> {}g')
print('Areas with hungry animals:')
for k, v in areas.items():
    if len(v) > 0:
        print(f'{k} : {len(v)}')

# 09. On the Way to Annapurna (exam problem) -----------------------------------
# --------------100 points ------------------------------------------
commands = input()
stores = {}

while commands != 'END':
    commands = commands.split('->')
    command = commands[0]
    store = commands[1]

    if command == 'Add':
        item = commands[2]
        if store not in stores:
            stores[store] = []

        if item.find(',') > 0:
            item = item.split(',')
            stores[store].extend(item)
        else:
            stores[store].append(item)

    elif command == 'Remove':
        if store in stores:
            stores.pop(store)

    commands = input()

# you need to sort both in descending
stores = dict(sorted(stores.items(), key=lambda s: s[0], reverse=True)) # (1) sort by key DESC
stores = dict(sorted(stores.items(), key=lambda s: -len(s[1])))         # (2) sort by value DESC

print('Stores list:')
for key, value in stores.items():
    print(key)
    for v in value:
        print(f'<<{v}>>')

# 10. Practice Sessions (exam problem) -----------------------------------------
# -------100 points -------------------
road_info = input()
roads = {}

while road_info != 'END':
    road_info = road_info.split('->')
    command = road_info[0]

    if command =='Add':
        road = road_info[1]
        racer = road_info[2]

        if road not in roads:
            roads[road] = [racer]
        else:
            roads[road].append(racer)

    elif command == 'Move':
        current_road = road_info[1]
        racer = road_info[2]
        next_road = road_info[3]

        for road in roads.keys():
            if road == current_road:
                if racer in roads[road]:
                    roads[road].remove(racer)
                    roads[next_road].append(racer)

    elif command == 'Close':
        road = road_info[1]
        if road in roads:
            roads.pop(road)

    road_info = input()

# sort descending by count of the items, key ascending
roads = dict(sorted(roads.items(), key=lambda r: (-len(r[1]), r[0])))

print('Practice sessions:')
for key, value in roads.items():
    print(key)
    for v in value:
        print(f'++{v}')


# ************More Exercises ***************************************************
