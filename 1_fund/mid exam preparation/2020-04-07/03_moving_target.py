
# https://github.com/ateneva/softuni_proj/wiki/fund_20200407_mid_exam_retake

# ---------------------03. Moving Target (Advanced Lists)---------------------------
# ----------------- 100 points ------------------------------

targets = list(map(lambda x: int(x), input().split(' ')))
command = input()

while command != 'End':
    command = command.split(' ')
    activity = command[0]
    idx = int(command[1])
    value = int(command[2])

    if activity == 'Shoot':
        if 0 <= idx < len(targets):
            if targets[idx]-value <= 0:
                targets.remove(targets[idx])
            else:
                targets[idx] -= value

    elif activity == 'Add':
        if 0 <= idx < len(targets):
            targets.insert(idx, value)
        else:
            print("Invalid placement!")

    elif activity == 'Strike':
        if 0 <= idx < len(targets)\
            and 0 <= idx-value < len(targets)\
            and 0 <= idx+value < len(targets):

            del targets[idx-1:idx+2]
        else:
            print("Strike missed!")

    command = input()

format_print = '|'.join(list(map(lambda x: str(x), targets)))
print(format_print)
