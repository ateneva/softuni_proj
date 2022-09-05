
# ----------------------------- 04.odd occurrences ----------------------------

'''
Write a program that extracts all elements from a given sequence of words
    that are present in it an odd number of times (case-insensitive).
    • Words are given on a single line, space separated.
    • Print the result elements in lowercase, in their order of appearance.
'''

def odd_occurences(word_sequence):
    words = word_sequence.split(" ")
    dictionary = {}

    for word in words:
        word = word.lower()

        if word not in dictionary:
            dictionary[word] = 0  # create a key
        dictionary[word] += 1  # count how many times the word occurs

    for (key, value) in dictionary.items():
        if value % 2 != 0:
            print(key, end=" ")

odd_occurences(input())

# OR

def odd_occurences_list(word_sequence):
    words = word_sequence.split(" ")
    occurrences = []

    for word in words:
        idx = words.index(word)
        word = word.lower()
        words[idx] = word

    for word in words:
        if words.count(word) % 2 != 0:
            if word not in occurrences:
                occurrences.append(word)

    print(" ".join(occurrences))

odd_occurences_list(input())

# OR # list comprehensions approach


words = input().split(" ")
occurrences = []

words_lower = [word.lower() for word in words]

for word in words_lower:
    if words_lower.count(word) % 2 != 0:
        if word not in occurrences:
            occurrences.append(word)

print(" ".join(occurrences))
