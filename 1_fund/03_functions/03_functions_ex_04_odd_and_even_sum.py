
# ----------------------04. odd and even sum -----------------------------------

'''
You will receive a single number. You have to write a function that returns
    the sum of all even and all odd digits from that number as a single string

'''

# --------------100 points --------------------
n = input()

def odd_or_sum(n):
    even = []
    odd = []
    for x in n:
        if int(x) % 2 == 0:
            even.append(int(x))
        elif int(x) % 2 != 0:
            odd.append(int(x))
    even = sum(even)
    odd = sum(odd)

    return [odd, even]

print(f'Odd sum = {odd_or_sum(n)[0]}, Even sum = {odd_or_sum(n)[1]}')
