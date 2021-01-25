
# -----------------------06. password validator --------------------------------

'''
Write a function that checks if a given password is valid. Password validations are:
    * The length should be 6 - 10 characters (inclusive)
    * It should consists only letters and digits
    * It should have at least 2 digits

If a password is valid print "Password is valid".

If it is NOT valid, for every unfulfilled rule print a message:
    * "Password must be between 6 and 10 characters"
    * "Password must consist only of letters and digits"
    * "Password must have at least 2 digits"
'''

# --------------100 points --------------------
password = input()

def validate(password):
    messages = []
    length = len(password)  >= 6 and len(password) <= 10

    # all returns True if all the conditions are met
    letters_and_digits = all([x.isdigit() or x.isalpha() for x in password ])

    # returns True if a character is a letter or num
    l_and_d = password.isalnum()
    num_digits = len([x for x in password if x.isdigit()]) >= 2

    # check validity
    if length and letters_and_digits and num_digits:
        messages.append("Password is valid")

    if not length:
        messages.append("Password must be between 6 and 10 characters")

    if not letters_and_digits:
        messages.append("Password must consist only of letters and digits")

    if not num_digits:
        messages.append("Password must have at least 2 digits")

    return messages

print('\n'.join(validate(password)))  # join on a new line
