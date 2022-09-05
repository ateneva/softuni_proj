
# ******************************************* Lab ***********************************************************

# 01. Match Full Name-----------------------------------------------
import re

names = input()

regex = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'
matches = re.findall(regex, names)

print(' '.join(matches))

# 02. Match Phone Number--------------------------------------------
import re

names = input()

regex = '(\\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\\b'
matches = re.findall(regex, names)

print(', '.join(matches))

# 03. Match Dates----------------------------------------------------
import re

names = input()

regex = '\\b(\d{2})([-./])([A-Z][a-z]{2})\\2(\d{4})\\b'
matches = re.findall(regex, names)

for match in matches:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')


# 04. Match Numbers--------------------------------------------------
import re

names = input()

regex = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
matches = re.finditer(regex, names)

for match in matches:
    print(match.group(0), end=' ')


# *************Exercises ******************************************************

# 01. Capture the Numbers------------------------------
import re

pattern = r'\d+'
text = input()

while True:
    if not text:
        break

    matches = re.findall(pattern, text)

    for match in matches:
        print(match, end=' ')

    text = input()


# 02. Find Variable Names---------------------------------
import re

pattern = r"\b[_]([a-zA-Z]*\b)"
text = input()

matches = re.findall(pattern, text)
variables = []

for match in matches:
    variables.append(match.strip())

print(','.join(variables), end=' ')


# 03. Find occurences of word in a sentence----------------


# 04. Extract Emails--------------------------------------


# 05. Furniture-------------------------------------------


# 06. Extract the Links-----------------------------------
