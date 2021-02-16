
# stream of letters ------------------------------------------------------------

letter = input()
output = ''
c_found = False
o_found = False
n_found = False
current_word = ''

while not letter == 'End':
    ascii_char = ord(letter)
    upper_case = ascii_char >= 65 and ascii_char <= 90
    lower_case = ascii_char >= 97 and ascii_char <= 122

    if upper_case or lower_case:

        if letter == 'c' and not c_found:
            c_found = True
            letter = input()
            if c_found and o_found and n_found:
                output += f'{current_word} '
                current_word = ''
                c_found = False
                o_found = False
                n_found = False
            continue   # skip to the following iteration

        if letter == 'o' and not o_found:
            o_found = True
            letter = input()
            if c_found and o_found and n_found:
                output += f'{current_word} '
                current_word = ''
                c_found = False
                o_found = False
                n_found = False
            continue

        if letter == 'n' and not n_found:
            n_found = True
            letter = input()
            if c_found and o_found and n_found:
                output += f'{current_word} '
                current_word = ''
                c_found = False
                o_found = False
                n_found = False
            continue

        current_word += letter

    letter = input()

print(output)
