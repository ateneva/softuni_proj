
# ************************************************ Group 2 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20190630_mid_exam_group_2

# ---------------------------------02. Tasks Planner (Lists Basic)---------------------------------------------

# ------- 30 points -----------------------
hours = list(map(int, input().split(" ")))
command = input()
tasks = len(hours)

while command != "End":
    command = command.split(" ")
    do = command[0]

    if do == 'Complete':
        idx = int(command[1])
        if 0 <= idx < len(hours):
            hours[idx] = 0

    elif do == 'Change':
        idx = int(command[1])
        time = int(command[2])
        if 0 <= idx < len(hours):
            hours[idx] = time

    elif do == 'Drop':
        idx = int(command[1])
        if 0 <= idx < len(hours):
            hours[idx] = -1

    elif do == 'Count':
        which = command[1]
        completed = hours.count(0)
        incomplete = [h for h in hours if h > 0]
        dropped = [d for d in hours if d < 0]

        if which == 'Completed':
            print(completed)

        elif which == 'Incomplete':
            print(len(incomplete))

        elif which == 'Dropped':
            print(len(dropped))

    command = input()

print(" ".join(map(str, incomplete)))
