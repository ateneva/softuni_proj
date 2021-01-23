
# ************************************************ Group 1 ****************************************************

# ---------------------------------03. Last Stop (Lists Advanced) -------------------------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20190310_mid_exam_group_1

# ------- 100 points --------------------------

paintings = list(map(int, input().split(" ")))
instructions = input()

while instructions != "END":
    instructions = instructions.split(" ")
    command = instructions[0]
    if command != "Reverse":
        painting = int(instructions[-1])
    else:
        painting = instructions[-1]

    #print(paintings, command)

    if command == 'Change':
        painting_num = int(instructions[1])
        if painting_num in paintings:
            idx = paintings.index(painting_num)
            paintings.remove(painting_num)
            paintings.insert(idx, painting)

    elif command == "Hide":
        if painting in paintings:
            paintings.remove(painting)

    elif command == "Switch":
        painting_one = int(instructions[1])

        if painting_one in paintings:
            pos_one = paintings.index(painting_one)
            if painting in paintings:
                pos_two = paintings.index(painting)

                paintings[pos_one], paintings [pos_two] = paintings [pos_two], paintings[pos_one]

    elif command == "Insert":
        place = int(instructions[1])
        if place < len(paintings):
            paintings.insert(place + 1, painting)
        else:
            pass

    elif command == "Reverse":
        paintings.reverse()

    #print(paintings, instructions, command, painting)

    instructions = input()

output = " ".join(map(str, paintings))
print(output)
