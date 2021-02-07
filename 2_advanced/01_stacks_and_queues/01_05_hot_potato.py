
# --------------Problem 5 (queue): Hot Potato-----------------------------------

'''
Hot potato is a game in which children form a circle and start passing a hot
potato. The counting starts with the first kid. Every nth toss the child left
the potato leaves the game. When a kid leaves the game, it passes the potato along.

This continues until there is only one kid left.
Create a program that simulates the game of Hot Potato.
Print every kid that is removed from the circle.
In the end, print the kid that is left last.
'''

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

solve(input().split(' '), int(input()))
