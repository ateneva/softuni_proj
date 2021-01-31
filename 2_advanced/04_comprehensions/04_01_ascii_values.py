
# ---------------01. ascii values ---------------------------------

'''
Write program that receives a list of characters
and creates a dictionary with each character as a key
    and its ASCII value as a value
'''

def ascii_values(chars):
    characters = chars.split(", ")
    asc_codes = {ch:ord(ch) for ch in characters}
    return asc_codes

print(ascii_values(input()))
