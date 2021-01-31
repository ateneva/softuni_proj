
# --------------------------02. no vowels--------------------------------------

'''
Using a comprehension write a program that receives a text and removes all
the vowels from it. Print the new text string after removing the vowels.
'''

def remove_vowels(text):
    consonants = [ch for ch in text
                  if ch not in ['a', 'o', 'u', 'e', 'i']]
    return "".join(consonants)

print(remove_vowels(input()))
