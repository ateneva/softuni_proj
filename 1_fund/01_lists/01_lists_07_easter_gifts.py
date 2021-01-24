
# ------------------------07. easter gifts (exam problem) ----------------------

'''
As a good friend, you decide to buy presents for your friends.
**Create a program that helps you plan the gifts for your friends and family.**

First, you are going to receive the gifts you plan on buying оn a single line,
    separated by space, in the following format:
    `"{gift1} {gift2} {gift3}… {giftn}"`

Then you will start receiving commands until you read the "No Money" message.
There are three possible commands:
* "OutOfStock {gift}"
    > Find the gifts with this name in your collection, if there are any, and change their values to "None".

* "Required {gift} {index}"
    > Replace the value of the current gift on the given index with this gift, if the index is valid.

* "JustInCase {gift}"
    > Replace the value of your last gift with this one.

In the end, print the gifts on a single line, except the ones with value "None",
    separated by a single space in the following format:
    `"{gift1} {gift2} {gift3}… {giftn}"`

'''

gifts = input().split(' ')
wish = input()

while wish != 'No Money':
    tokens = wish.split(' ')

    if tokens[0] == 'OutOfStock':
        gift = tokens[1]
        for g in range(len(gifts)):
            if gifts[g] == gift:
               gifts[g] = 'None'           # ideally we want to remove it from the list

    elif tokens[0] == 'Required':
        idx = int(tokens[2])
        if idx >= 0 and idx < len(gifts):  # check if the index is valid
            gifts[idx] = tokens[1]

    elif tokens[0] == 'JustInCase':
        gifts[-1] = tokens[1]              # replace the last present with the current present

    wish = input()

result = []
for gift in gifts:
    if gift != 'None':
        result.append(gift)

print(' '.join(result))
