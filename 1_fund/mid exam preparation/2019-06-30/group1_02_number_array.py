
# ************************************************ Group 1 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20190630_mid_exam_group_1

# ---------------------------------02. Number Array (Lists Basic)---------------------------------------------

# --------------90 points (1x runtime error)-------------------------
numbers = list(map(int, input().split(" ")))
command = input()

while command != "End":
    command = command.split(" ")
    do = command[0]

    #print(numbers, command, do)

    if do == 'Switch':
        idx = int(command[1])
        if 0 <= idx < len(numbers):
            num = numbers[idx]
            numbers[idx] = num * -1

    elif do == 'Change':
        idx = int(command[1])
        value = int(command[2])

        if 0 <= idx < len(numbers):
            num = numbers[idx]
            numbers[idx] = value

    elif do == 'Sum':
        num_type = command[1]
        if num_type == 'Negative':
            negatives = [n for n in numbers if n < 0]
            print(sum(negatives))

        elif num_type == "Positive":
            positives = [p for p in numbers if p >= 0]
            print(sum(positives))

        elif num_type == "All":
            print(sum(numbers))

    positives = [p for p in numbers if p >= 0]

    command = input()
# print(numbers)
print(" ".join(map(str, positives)))
