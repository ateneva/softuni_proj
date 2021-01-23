
# ---------------------------------01. Disneyland Journey (Conditional Statements)-------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20191210_mid_exam_retake

# ---------------------------------02. Archery Tournament (Lists Basic)------------------------------------

targets = list(map(int,input().split("|")))
command = input()
points = 0

while command != "Game over":
    command = command.split("@")
    do = command[0]

    #print(targets, do, command)

    if do == 'Shoot Left':
        start = int(command[1])
        length = int(command[2])
        idx = len(targets) - ((start + length) % len(targets))

        if 0 <= start < len(targets):
            targets[idx] -= 5
            points += 5

    elif do == 'Shoot Right':
        start = int(command[1])
        length = int(command[2])
        idx = (start + length) % len(targets)

        if 0 <= start < len(targets):
            targets[idx] -= 5
            points += 5

    elif do == 'Reverse':
        targets.reverse()

    command = input()

print(" - ".join(map(str,targets)))
print(f"Iskren finished the archery tournament with {points} points!")
