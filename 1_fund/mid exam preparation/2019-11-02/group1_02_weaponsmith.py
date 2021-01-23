
# ************************************************ Group 1 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20191102_mid_exam_group_1

# ---------------------------------02. Weaponsmith (Lists Basic)---------------------------------------------

# ------- 100 points -----------------------

parts = input().split("|")
command = input()

while command != 'Done':
    do = command.split(" ")[0]
    #print(parts, command, do)

    if do == 'Move':
        direction = command.split(" ")[1]
        idx = int(command.split(" ")[2])
        old_idx = idx

        if idx < len(parts):
            if direction == 'Left':
                idx = idx-1
            elif direction == 'Right':
                idx = idx + 1

            if idx >= 0:
                to_move = parts.pop(old_idx)
                parts.insert(idx, to_move)

    elif do == 'Check':
        num_type = command.split(" ")[1]
        if num_type == 'Even':
            evens = [e for e in parts if parts.index(e) % 2 == 0]
            print(" ".join(evens))

        elif num_type == 'Odd':
            odds = [o for o in parts if parts.index(o) % 2 != 0]
            print(" ".join(odds))

    command = input()

weapon = "".join(parts)
print(f"You crafted {weapon}!")
