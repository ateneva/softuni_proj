
# cake--------------------------------------------------------------------------
width = int(input())
length = int(input())
cake = input()
slices = 0

while not cake == 'STOP':
    cake = int(cake)
    slices += cake

    if slices > width*length:
        left = abs(slices - width*length)
        print(f'No more cake left! You need {left} pieces more.')
        break
    cake = input()

else:
    left = abs(slices - width*length)
    print(f'{left} pieces are left.')
