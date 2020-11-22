
# Problem statement in 
# https://github.com/ateneva/softuni_proj/wiki/fund_lists_07.easter_gifts

# ------------------------07. easter gifts (exam problem) ------------------------------------------------------

gifts = input().split(' ')
wish = input()

while wish != 'No Money':
    tokens = wish.split(' ')

    if tokens[0] == 'OutOfStock':
        gift = tokens[1]
        for g in range(len(gifts)):
            if gifts[g] == gift:
               gifts[g] = 'None'           # ideally we want to remove it from the list

    elif tokens[0] == 'Required':
        idx = int(tokens[2])
        if idx >= 0 and idx < len(gifts):  # check if the index is valid
            gifts[idx] = tokens[1]

    elif tokens[0] == 'JustInCase':
        gifts[-1] = tokens[1]              # replace the last present with the current present

    wish = input()

result = []
for gift in gifts:
    if gift != 'None':
        result.append(gift)

print(' '.join(result))
