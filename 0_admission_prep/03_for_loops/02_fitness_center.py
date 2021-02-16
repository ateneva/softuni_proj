
# ******** 05.fitness center (for loop) ****************************************

visitors = int(input())
back = 0
chest = 0
legs = 0
abs = 0
shake = 0
bar = 0

for visitor in range(visitors):
    activity = input()

    if activity == 'Back':
        back += 1

    elif activity == 'Chest':
        chest += 1

    elif activity == 'Legs':
        legs += 1

    elif activity == 'Abs':
        abs += 1

    elif activity == 'Protein shake':
        shake += 1

    elif activity == 'Protein bar':
        bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{(back + chest + legs + abs)/visitors*100:.2f}% - work out")
print(f"{(shake + bar)/visitors*100:.2f}% - protein")
