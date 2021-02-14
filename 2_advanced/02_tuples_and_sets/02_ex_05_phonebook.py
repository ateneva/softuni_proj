
# ----------------------problem 5: phonebook -----------------------------------

'''
Write a program that receives info from the console about people and their phone numbers.
You are free to choose the way the data is entered; each entry should have
    a name and a number (both strings).
    If you receive a name that already exists in the phonebook, update its number.
After filling the phonebook, you will receive a number – N.
Your program should be able to perform a search of a contact by name
    and print her details in format "{name} -> {number}".
In case the contact isn't found, print "Contact {name} does not exist."
'''

phonebook = {}
while True:
    entries = input()
    phones = entries.split("-")

    if len(entries) > 1:
        record = {phones[0]: phones[1] for phone in phones}
        phonebook.update(record)

    elif len(entries) == 1:
        break

#print(entries)
#print(phonebook)

for _ in range(int(entries)):
    search = input()
    if search in phonebook.keys():
        found = {person: phone for (person, phone) in phonebook.items() if search == person}
        for contact, number in found.items():
            print(f'{contact} -> {number}')
    else:
        print(f'Contact {search} does not exist.')
