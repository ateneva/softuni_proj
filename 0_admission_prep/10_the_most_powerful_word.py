

 # *************** 06.the most powerful word (nested loop) *********************

word = input()
strongest = 0
most_powerful_word = ''

while word != 'End of words':
    strength = 0

    for char in word:
        i = ord(char)
        strength += i

    if word[0] in ('a', 'e', 'i', 'o', 'u', 'y') \
        or word[0] in ('A', 'E', 'I', 'O', 'U', 'Y'):
        strength *= len(word)

    else:
        strength //= len(word)

    if strength >= strongest:
        strongest = strength
        most_powerful_word = word

    word = input()

print(f"The most powerful word is {most_powerful_word} - {strongest}")
