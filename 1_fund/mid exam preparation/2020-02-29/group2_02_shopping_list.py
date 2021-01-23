
# https://github.com/ateneva/softuni_proj/wiki/fund_20200229_mid_exam_group_2

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
