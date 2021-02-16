
# moving-----------------------------------------------------------------------

width = int(input())
length = int(input())
height = int(input())
boxes = input()
box_volume = 0
isFree = True

while not boxes == 'Done':
    boxes = int(boxes)
    box_volume += boxes

    if box_volume > (width * length * height):
        isFree = False
        break

    boxes = input()  # breaking the endless looping

space_left = abs((width * length * height) - box_volume)
if isFree: # boolean take a value of true by default
    print(f'{space_left} Cubic meters left.')
else:
    print(f'No more free space! You need {space_left} Cubic meters more.')
