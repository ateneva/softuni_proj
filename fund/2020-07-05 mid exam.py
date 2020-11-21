
# --------------------01. Softuni Reception (Conditional Statements)---------------------------
# # https://github.com/ateneva/softuni_proj/wiki/fund_20200705_mid_exam

# --------------------- 90 points --------------------------
questions = []
hours = 1

for i in range(1, 4):
    efficiency = int(input())
    questions.append(efficiency)

students = int(input())
queue = sum(questions)

while students > queue:
    students -=queue
    hours += 1

    if hours % 4 ==0:
        students -= 0
        hours += 1

print(f"Time needed: {hours}h.")


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


# --------------------03. Numbers  (Lists Advanced)---------------------------

# ------------------- 100 points --------------------------

elements = list(map(lambda x: int(x),input().split(' ')))
avg_value = sum(elements) / len(elements)

new_sequence = [e for e in elements if e > avg_value]
filtered_list = list(map(lambda x: str(x),sorted(new_sequence, reverse=True)))[:5]

if len(filtered_list) > 0:
    print(' '.join(filtered_list))
else:
    print('No')
