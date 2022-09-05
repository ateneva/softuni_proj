
# ********************Lab ******************************************************

# 01. Reverse Strings-------------------------------
string = input()

while string != 'end':
    string_reversed = ""

    for st in reversed(string):
        string_reversed += st

    print(string + ' = ' + string_reversed)

    string = input()


# 02. Repeat Strings--------------------------------
strings = input().split(" ")
result = ""

for word in strings:
    length = len(word)
    result += word * length

print(result)

# 03. Substring--------------------------------------
first = input()
second = input()

while first in second:
    second = second.replace(first,'')

print(second)

# 04. Text Filter------------------------------------
banned = input().split(", ")
text = input()

for ban in banned:
    if ban in text:
        text = text.replace(ban, "*"*len(ban))

print(text)

# 05. Digits, Letters and Other
string = input()
digits = ''
letters = ''
others = ''

for ch in string:
    if ch.isdigit():
        digits +=ch

    elif ch.isalpha():
        letters +=ch

    else:
        others +=ch

print(digits)
print(letters)
print(others)

# **************************Exercises ******************************************

# 01. Valid Username-----------------------------------------------
usernames = input().split(", ")
valid = []

for username in usernames:
    if 3<=len(username) <=16:
        if username.isalnum():
            if username == username.strip():
                valid.append(username)

        if '-' in username:
            valid.append(username)

        if '_' in username:
            valid.append(username)

for v in valid:
    print(v)

# 02. Character Multiplier------------------------------------------
string = input().split(" ")
first = string[0]
second = string[1]
total_sum = 0

for i in range(max(len(first), len(second))):
    if i < len(first) and i < len(second):
        total_sum += ord(first[i]) * ord(second[i])
    else:
        if i < len(first):
            total_sum += ord(first[i])
        else:
            total_sum += ord(second[i])

print(total_sum)

# 03. Extract File--------------------------------------------------
path = input().split('\\')

for p in path:
    if p.find('.'):
        file = p.split(".")

filename = file[0]
extension = file[1]

print(f'File name: {filename}')
print(f'File extension: {extension}')

# 04. Caeser Cipher-------------------------------------------------
string = input()
coded = ''

for s in string:
    c = ord(s) + 3
    coded +=chr(c)

print(coded)

# 05. Emoticon Finder-----------------------------------------------
string = input()

for s in range(len(string)):
    if string[s] == ':':

        # eliminate regular semiclon in the middle or end of string
        if s + 1 < len(string) and string[s+1] != ' ':
            print(f':{string[s+1]}')

# 06. Replace Repeating Chars---------------------------------------------------
string = input()
i = 0

while i < len(string) - 1:
    if string[i] == string[i+1]:
        string = string.replace(f"{string[i]}{string[i+1]}", f'{string[i]}')
        i = 0
    else:
        i+= 1

print(string)

# 07. String Explosion----------------------------------------------------------
# Tanya
explosion = input()
result = ''
i = 0
count = 0

while i < len(explosion):
    if explosion[i] != '>':
        result += explosion[i]
        i += 1
    else:
        result += '>'
        i += 1
        count += int(explosion[i])
        while count >0 and explosion[i] != '>':
            i += 1
            count -= 1
            if i >= len(explosion):
                break
print(result)

# Slavi
explosion = input()
power = 0
i = 0

while i < len(explosion):
    ch = explosion[i]

    if ch == '>':
        power += int(explosion[i+1])

    elif power > 0:
        explosion = explosion[:i] + explosion[i+1:]
        i -= 1
        power -=1
        pass

    i += 1
print(explosion)

# 08. Letters Change Numbers----------------------------------------------------



# 09. Rage Quit-----------------------------------------------------------------



# 10. Winnning Ticket-----------------------------------------------------------
