
# 02.letter combinations--------------------------------------------------------

first = input()
second = input()
third = input()
count = 0

for i in range(ord(first), ord(second)+1):
    for j in range(ord(first), ord(second)+1):
        for k in range(ord(first), ord(second)+1):
            if chr(i) != third and chr(j) != third and chr(k) != third:
                count += 1
                print(f'{chr(i)}{chr(j)}{chr(k)} ', end='')
print(count)
