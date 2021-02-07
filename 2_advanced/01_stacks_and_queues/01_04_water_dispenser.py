
# --------------Problem 4 (queue): water Dispenser------------------------------

'''
Write a program that reads on the first line the starting quantity of water
in a dispenser. Then on the next few lines you will be given the names of
some people that want to get water (each on separate line) until
you receive the command "Start". Add those people in a queue.

Finally, you will receive some commands until the command "End":
- {liters} - Litters that the current person in the queue wants to get.
    Check if there is enough water in the dispenser for that person.
    - If there is enough water, print "{person_name} got water" and remove him/her from the queue.
    - Otherwise, print "{person} must wait" and remove the person from the queue
    without reducing the water in the dispenser
-	refill {liters} - add the given litters in the dispenser.

At the end print how many litters of water are left in the format: "{left_liters} liters left"
'''

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
