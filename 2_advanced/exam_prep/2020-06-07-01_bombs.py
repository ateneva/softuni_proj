
'''
You will be given two sequences of integers, representing bomb effects and bomb casings.
You need to start from the first bomb effect and try to mix it with the last bomb casing.
If the sum of their values is equal to any of the materials in the table below
    – create the bomb corresponding to the value and remove both bomb materials.
    Otherwise, just decrease the value of the bomb casing by 5.
You need to stop combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.
Bombs:
    - Datura Bombs: 40
    - Cherry Bombs: 60
    - Smoke Decoy Bombs: 120
To fill the bomb pouch, Ezio needs three of each of the bomb types

On the first line, print:
    - if Ezio succeeded to fulfill the bomb pouch:
        "Bene! You have successfully filled the bomb pouch!"
    - if Ezio didn't succeed to fulfill the bomb pouch:
        "You don't have enough materials to fill the bomb pouch."

On the second line, print all bomb effects left:
    - If there are no bomb effects: "Bomb Effects: empty"
    - If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"

On the third line, print all bomb casings left:
    - If there are no bomb casings: "Bomb Casings: empty"
    - If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"

Then, you need to print all bombs and the count you have of them, ordered alphabetically:
    - "Cherry Bombs: {count}"
    - "Datura Bombs: {count}"
    - "Smoke Decoy Bombs: {count}"
'''

from collections import deque

bomb_effects = deque([int(i) for i in input().split(", ")])
bomb_casings = [int(i) for i in input().split(", ")]

#print(bomb_effects)
#print(bomb_casings)

datura_bombs = 0        # 40
cherry_bombs = 0        # 60
smoke_decoy_bombs = 0   # 120
full_pouch = False

while bomb_effects:
    if len(bomb_casings) > 0:
        if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
            full_pouch = True
            break
        else:
            bomb_effect = bomb_effects[0]
            bomb_casing = bomb_casings[-1]
            bomb = (bomb_effect + bomb_casing)
            if bomb == 40:
                datura_bombs += 1
                bomb_effects.popleft()
                bomb_casings.pop()

            elif bomb == 60:
                cherry_bombs += 1
                bomb_effects.popleft()
                bomb_casings.pop()

            elif bomb == 120:
                smoke_decoy_bombs += 1
                bomb_effects.popleft()
                bomb_casings.pop()

            else:
                bomb_casings[-1] -= 5

if full_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects) > 0:
    print(f'Bomb Effects: {", ".join([str(i) for i in bomb_effects])}')
else:
    print("Bomb Effects: empty")

if len(bomb_casings) > 0:
    print(f'Bomb Casings: {", ".join([str(i) for i in bomb_casings])}')
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")
