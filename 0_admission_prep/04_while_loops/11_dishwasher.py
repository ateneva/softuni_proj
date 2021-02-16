
# diswasher -------------------------------------------------------------------

bottles = int(input())
detergent = bottles * 750
cutlery = ''
load = 0
used = 0
dishes = 0
pots = 0

while cutlery != 'End':    # until input = "End" or we've run out of detergent
    cutlery = input()
    load += 1

    if cutlery == 'End':
        if used <= detergent:
            print(f'Detergent was enough!')
            print(f'{dishes} dishes and {pots} pots were washed.')
            print(f'Leftover detergent {abs(detergent - used)} ml.')

        else:
            print(f'Not enough detergent, {abs(detergent - used)} ml. more necessary!')
        break

    if load % 3 == 0:
        used += int(cutlery) * 15
        pots += int(cutlery)

    else:
        used += int(cutlery) * 5
        dishes += int(cutlery)

    if used > detergent:
        print(f'Not enough detergent, {abs(detergent - used)} ml. more necessary!')
        break
        # program ends when "End" is passed on as input or when detergent is over
