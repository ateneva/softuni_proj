
#------------------------Problem 1: Reverse Strings----------------------------
#-----100 points ------------
text = input()
stack = []
reversed_text = []

for ch in text:         # convert string to list
    stack.append(ch)

while stack:
    ch = stack.pop()
    reversed_text.append(ch)

print(''.join(reversed_text))

# -----approach 2--------------
def reverse_string(text):
    return text[::-1]

print(reverse_string(input()))

# -----approach 3-------------
text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())

print("".join(stack))


# -----------------Problem 2: Matching brackets---------------------------------

text = input()
brackets = []

for i in range(len(text)):
    if text[i] == "(":
        brackets.append(i)

    elif text[i] == ")":
        start_index = brackets.pop()
        print(text[start_index:i + 1])


#------------------Problem 3 (queue): Supermarket-------------------------------
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

# --------------Problem 4 (queue): water Dispenser------------------------------
from collections import deque

water = int(input())
people = deque()

while True:
    command = input()
    if command == 'Start':
        break
    people.append(command)

while True:
    command = input().split(' ')
    if command[0] == 'End':
        print(f'{water} liters left')
        break
    elif command[0] == 'refill':
        water += int(command[1])
    else:
        person_water = int(command[0])
        person = people.popleft()

        if person_water <= water:
            water -= person_water
            print(f'{person} got water')
        else:
            print(f'{person} must wait')

# --------------Problem 5 (queue): Hot Potato-----------------------------------
from collections import deque

def solve(people, tosses):
    people = deque(people)
    toss = 0

    while people:
        toss += 1
        person = people.popleft()
        if toss == tosses:
            if people:
                toss = 0
                print(f'Removed {person}')
            else:
                print(f'Last is {person}')
        else:
            people.append(person)

solve(input().split(' '), int(input())
        )
