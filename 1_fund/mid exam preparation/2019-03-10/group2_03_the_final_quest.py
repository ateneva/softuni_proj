
# ********************************************** Group 2 *********************************************************

# ---------------------------------03. The Final Quest (Lists Advanced)---------------------------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20190310_mid_exam_group_2

# ------- 83 points /2 x incorrect answer/-----------

message = input().split(" ")
instructions = input()

while instructions != 'Stop':
    instructions = instructions.split(" ")
    command = instructions[0]

    if command == 'Delete':
        delete_idx = int(instructions[1]) + 1
        if delete_idx < len(message):
            del message[delete_idx]

    elif command == 'Swap':             # if swap or replace, just use the indexing
        word_one = instructions[1]
        word_two = instructions[2]

        if word_one in message:
            if word_two in message:
                idx_one = int(message.index(word_one)) # save the position where the  word was
                idx_two = int(message.index(word_two)) # save the position where the word was

                # message.remove(word_one)
                # message.insert(idx_one, word_two)
                # message.remove(word_two)
                # message.insert(idx_two, word_one)
                message[idx_one], message[idx_two] = message[idx_two], message[idx_one]

    elif command == 'Put':
        word = instructions[1]
        position = int(instructions[2])

        if position < len(message):
            message.insert(position-1, word)

    elif command == 'Sort':
        message = sorted(message, reverse=True)   # function --> can be applied on any iterable
        message.sort(reverse=True)                # method  --> only applicable to lists

    elif command == 'Replace':
        word_one = instructions[1]
        word_two = instructions[2]

        if word_two in message:
            idx = message.index(word_two) # save the position
            message.remove(word_two)
            message.insert(idx, word_one)

    #print(message, instructions, command)

    instructions = input()

print(" " .join(message))
