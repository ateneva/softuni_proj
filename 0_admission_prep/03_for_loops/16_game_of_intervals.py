
# game of intervals ------------------------------------------------------------

moves = int(input())
score = 0
zero_to_nine = 0
ten_to_nineteen = 0
twenty_to_twenty_nine = 0
thirty_to_thirty_nine = 0
forty_to_fifty = 0
invalid_numbers = 0

for move in range(moves):
    i = int(input())

    if i >= 0 and i <= 9:
        score += i * 0.20
        zero_to_nine += 1

    elif i >= 10 and i <= 19:
        score += i * 0.30
        ten_to_nineteen += 1

    elif i >= 20 and i <= 29:
        score += i * 0.40
        twenty_to_twenty_nine += 1

    elif i >= 30 and i <= 39:
        score += 50
        thirty_to_thirty_nine += 1

    elif i >= 40 and i <= 50:
        score += 100
        forty_to_fifty += 1

    elif i > 50 or i < 0:
        score /= 2
        invalid_numbers += 1

print(f'{score:.2f}')
print(f'From 0 to 9: {zero_to_nine/moves*100:.2f}%')
print(f'From 10 to 19: {ten_to_nineteen/moves*100:.2f}%')
print(f'From 20 to 29: {twenty_to_twenty_nine/moves*100:.2f}%')
print(f'From 30 to 39: {thirty_to_thirty_nine/moves*100:.2f}%')
print(f'From 40 to 50: {forty_to_fifty/moves*100:.2f}%')
print(f'Invalid numbers: {invalid_numbers/moves*100:.2f}%')
