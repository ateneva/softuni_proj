

# spaceship (conditional statements)********************************************
import math as m

spaceship_width = float(input())
spaceship_length = float(input())
spaceship_height = float(input())
avg_height = float(input())

l = 2
w = 2
h = 0.40 + avg_height

spaceship_volume = spaceship_width * spaceship_length * spaceship_height
room_volume = l * w * h
participants = m.floor(spaceship_volume/room_volume)

# print(spaceship_volume)
# print(room_volume)
# print(participants)

if participants < 3:
    print("The spacecraft is too small.")

elif participants >= 3 and participants < 10:
    print(f'The spacecraft holds {participants} astronauts.')

elif participants >= 10:
    print('The spacecraft is too big.')
