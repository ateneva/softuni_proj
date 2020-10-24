
# ************************************************ Group 2 ****************************************************

# ---------------------------------01. Gift Box Coverage (Conditional Statements)---------------------------

# ------- 100 points -----------------------
size = float(input())
total_paper = int(input())
single_sheet_cover = float(input())
sides = 6

total_area = size ** 2 * sides
area_covered = 0

for paper in range(1, total_paper + 1):
    if paper % 3 == 0:
        single_sheet = single_sheet_cover * 0.25
    else:
        single_sheet = single_sheet_cover

    area_covered += single_sheet

percentage = area_covered / total_area * 100
print(f"You can cover {percentage:.2f}% of the box.")

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
