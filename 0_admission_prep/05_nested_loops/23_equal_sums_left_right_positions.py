
# equal sums (left/right positions) -------------------------------------------

a = int(input())
b = int(input())

for num in range(a, b+1):
    num = str(num)

    first = int(num[0])
    second = int(num[1])
    third = int(num[2])
    fourth = int(num[3])
    fifth = int(num[4])

    left_position = first + second
    right_position = fourth + fifth
    middle = third

    if left_position == right_position:
        print(num, end=' ')
    else:
        if left_position > right_position:
            right_position += middle

            if left_position == right_position:
                print(num, end=' ')
        else:
            left_position += middle

            if left_position == right_position:
                print(num, end=' ')
