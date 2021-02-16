

# equal sums (even/odd positions) ----------------------------------------------

a = int(input())
b = int(input())

for num in range(a, b+1):
    num = str(num)

    first = int(num[0])
    second = int(num[1])
    third = int(num[2])
    fourth = int(num[3])
    fifth = int(num[4])
    sixth = int(num[5])

    odd_position = fifth + third + first
    even_position = sixth + fourth + second

    are_equal = odd_position == even_position

    if are_equal:
        print(num, end=' ')


# equal sums (even/odd positions - 2nd approach) -------------------------------
a = int(input())
b = int(input())

for num in range(a, b+1):
    num = str(num)
    odd_position = 0
    even_position = 0

    for index in range(len(num)):
        if index % 2 == 0:
            even_position += int(num[index])
        else:
            odd_position += int(num[index])

    are_equal = odd_position == even_position

    if are_equal:
        print(num, end=' ')
