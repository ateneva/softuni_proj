
# 09.sum of two numbers-------------------------------------------------------------

start = int(input())
end = int(input())
magic_number = int(input())
comb = 0
is_found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        comb += 1
        magic = comb
        if ((i + j) or (j + i) )== magic_number:
            is_found = True
            break

    if is_found:
        print(f"Combination N:{comb} ({i} + {j} = {magic_number})")
        break

if not is_found:
    print(f"{comb} combinations - neither equals {magic_number}")
