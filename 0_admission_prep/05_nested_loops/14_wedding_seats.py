
# 06.wedding seats------------------------------------------------------------------

aisle = input()
rows = int(input())
seats = int(input())
count_seats = 0

for a in range(65, ord(aisle) + 1):
    if a > 65:
        rows += 1   # rows increase by 1 in every sector after A

    for r in range(1, rows + 1):
        if r % 2 != 0:                # seats in even rows are by 2 more
            for s in range(97, 97 + seats):
                print(f'{chr(a)}{r}{chr(s)}')
                count_seats += 1
        else:
            even_seats = seats + 2
            for s in range(97, 97 + even_seats):
                print(f'{chr(a)}{r}{chr(s)}')
                count_seats += 1

print(count_seats)
