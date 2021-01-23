
# ************************************************ Group 2 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20190630_mid_exam_group_2

# ---------------------------------03. Froggy Squad (Lists Advanced) ----------------------------------------

# ------- 100 points -----------------------
frogs = input().split(" ")

while True:
    command = input().split(" ")
    do = command[0]

    if do == 'Join':
        frog = command[1]
        frogs.append(frog)

    elif do == 'Jump':
        frog = command[1]
        idx = int(command[2])

        if 0 <= idx < len(frogs):
            frogs.insert(idx, frog)

    elif do == 'Dive':
        idx = int(command[1])
        if 0 <= idx < len(frogs):
            del frogs[idx]

    elif do == 'First':
        count = int(command[1])
        if count <= len(frogs):
            print(" ".join(frogs[0:count]))
        else:
            print(" ".join(frogs[0:]))

    elif do == 'Last':
        count = int(command[1])
        if count <= len(frogs):
            last = frogs[-count:]
            print(" ".join(last))
        else:
            print(" ".join(frogs[-count:]))

    elif do == 'Print':
        how = command[1]
        #print(frogs, command)

        if how == 'Normal':
            frogs_normal = " ".join(frogs)
            print(f'Frogs: {frogs_normal}')
        else:
            frogs.reverse()
            print(f'Frogs: {" ".join(frogs)}')

        break
