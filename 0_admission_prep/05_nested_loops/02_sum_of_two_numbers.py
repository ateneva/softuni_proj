
# sum of two numbers------------------------------------------------------------

start = int(input())
end = int(input())
magic_num = int(input())
combination = 0
combinations = 0
isFound = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        combinations += 1
        if i + j == magic_num:
            isFound = True
            print(f'Combination N:{combinations} ({i} + {j} = {magic_num})')
            break
    if isFound:
        break

if isFound == False:
    print(f'{combinations} combinations - neither equals {magic_num}')
