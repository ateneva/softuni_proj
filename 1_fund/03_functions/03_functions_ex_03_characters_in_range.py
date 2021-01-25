
# --------------------03. characters in range ----------------------------------

'''
Write a function that receives two characters
    and returns a single string with all the characters in between them according to the ASCII code.
'''

# --------------100 points --------------------
char1 = input()
char2 = input()

def chars(char1, char2):
    rng = []
    for char in range(ord(char1) + 1, ord(char2)):
        rng.append(chr(char))

    return ' '.join(rng)

print(chars(char1, char2))
