
 # ******************* 06.baking competition (nested loop) *********************

participants = int(input())
sold = 0
earned = 0

for participant in range(1, participants + 1):
    name = input()
    bakery = input()

    cookies = 0  # need to be nullified for the next participant
    cakes = 0
    waffles = 0

    while not bakery == 'Stop baking!':
        baked = int(input())

        if bakery == 'cookies':
            cookies += baked
            earned += (baked * 1.50)

        elif bakery == 'cakes':
            cakes += baked
            earned += (baked * 7.80)

        elif bakery == 'waffles':
            waffles += baked
            earned += (baked * 2.30)

        bakery = input()

    print(f"{name} baked {cookies} cookies, {cakes} cakes and {waffles} waffles.")
    sold += (cookies + cakes + waffles)

print(f"All bakery sold: {sold}")
print(f"Total sum for charity: {earned:.2f} lv.")
