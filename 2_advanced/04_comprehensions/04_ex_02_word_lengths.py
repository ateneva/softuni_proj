
# ------------------------02. word lengths ------------------------------------

'''
Using list comprehension, write a program that receives some strings separated
by comma and space ", " and prints on the console each string with its length
in the format: "{first_str} -> {first_str_len}, {second_str} -> {second_str_len}"
'''

# approach 1: use dictionary and list
def words_list(words_seq):
    words = words_seq.split(", ")
    word_list = {}

    for word in words:
        if word not in word_list:
            word_list[word] = len(word)

    final_list = []
    for word, word_length in word_list.items():
        print_format = f"{word} -> {word_length}"
        final_list.append(print_format)

    return  ", ".join(final_list)
print(words_list(input()))

# approach 2: use dictionary and list comprehension
def neater_approach(words_seq):
    words = words_seq.split(", ")
    word_list = {}

    for word in words:
        if word not in word_list:
            word_list[word] = len(word)

    final_list = [f"{word} -> {word_length}"
                    for word, word_length in word_list.items()
                    ]

    return ", ".join(final_list)
print(neater_approach(input()))

# approach 3: use both dictionary comprehension and list comprehension
def shortest_approach(words_seq):
    words = words_seq.split(", ")
    word_list = {word: len(word) for word in words}

    final_list = [f"{word} -> {word_length}"
                    for word, word_length in word_list.items()
                    ]

    return ", ".join(final_list)
print(shortest_approach(input()))
