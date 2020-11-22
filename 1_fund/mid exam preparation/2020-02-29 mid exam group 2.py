
# --------------------01. National Court (Conditional Statements)---------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20200229_mid_exam_group_2

# --------------------- 90 points --------------------------
questions = []
hours = 1

for i in range(1, 4):
    efficiency = int(input())
    questions.append(efficiency)

people = int(input())
queue = sum(questions)

while people >= queue:
    people -=queue
    hours += 1

    if hours % 4 == 0:
        people -= 0
        hours += 1

print(f"Time needed: {hours}h.")

# --------------------02. Shopping List  (Basic Lists)---------------------------

# ------------------- 100 points --------------------------

initial_list = input().split('!')
command = input()
shopping_list = initial_list

while command != 'Go Shopping!':
    command = command.split(' ')
    activity = command[0]

    if activity != 'Correct':
        item = command[1]

        if activity == 'Urgent':
            if item not in shopping_list:
                shopping_list.insert(0, item)

        elif activity == 'Unnecessary':
            if item in shopping_list:
                shopping_list.remove(item)

        elif activity == 'Rearrange':
            if item in shopping_list:
                shopping_list.remove(item)
                shopping_list.append(item)

    else:
        item = command[2]
        old_item = command[1]
        if old_item in shopping_list:
            idx = shopping_list.index(old_item)
            shopping_list.remove(old_item)
            shopping_list.insert(idx, item)

    command = input()

print(', '.join(shopping_list))


# --------------------03. Heart Delivery (Lists Advances)---------------------------

# ------------------- 100 points --------------------------

houses = list(map(lambda x: int(x),input().split('@')))
command = input()
last_index = 0

while command != 'Love!':
    command = command.split(' ')
    activity = command[0]
    length = int(command[1])
    jump = last_index + length
    round = len(houses)

    if jump >= len(houses):
        jump = 0

    house = houses[jump]
    if house == 0:
        print(f"Place {jump} already had Valentine's day.")
    else:
        houses[jump] -= 2
        if houses[jump] == 0:
            print(f"Place {jump} has Valentine's day.")

    last_index = jump
    command = input()

print(f"Cupid's last position was {last_index}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([f for f in houses if f > 0])} places.")
