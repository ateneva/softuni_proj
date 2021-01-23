
# # https://github.com/ateneva/softuni_proj/wiki/fund_20200705_mid_exam

# --------------------02. Array Modifier Description  (Basic Lists)---------------------------
# ------------------- 100 points --------------------------

elements = list(map(lambda x: int(x),input().split(' ')))
command = input()

while command != 'end':
    command = command.split(' ')
    activity = command[0]

    if activity != 'decrease':
        idx_one = int(command[1])
        idx_two = int(command[2])

        if activity == 'swap':
            elements[idx_one], elements[idx_two] = elements[idx_two], elements[idx_one]

        elif activity == 'multiply':
            elements[idx_one] *= elements[idx_two]

    else:
        elements = [e-1 for e in elements]

    command = input()

print_format = list(map(lambda x: str(x),elements))
print(', '.join(print_format))
