
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



# approach 2 (define functions for key validation and printing format)

def validate_existing_key(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value

def print_dict(dictionary, template):
    for (key, value) in dictionary.items():
        print(template.format(key, value))


string = input()
chars_dict = {}

for char in string:
    if char == ' ':  # validate for spaces
        continue

    validate_existing_key(chars_dict, char)
    chars_dict[char] += 1

print_dict(chars_dict, '{} -> {}')
