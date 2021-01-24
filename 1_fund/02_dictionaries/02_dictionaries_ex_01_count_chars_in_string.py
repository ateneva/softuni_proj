
# ---------------------01. Count characters in a string -----------------------

'''
Write a program that counts all characters in a string except for space (' ').
Print all the occurrences in the following format:
{char} -> {occurrences}
'''

string = input()
chars_dict = {}

for char in string:
    if char == ' ':  # validate for spaces
        continue

    if char not in chars_dict:   # ensure that a key is always created
        chars_dict[char] = 0

    chars_dict[char] += 1

for (key,value) in chars_dict.items():
    print(f'{key} -> {value}')
