
# --------------------------01. word filter -----------------------------------

'''
Using comprehension, write a program that receives some strings separated by
space and take only those words, whose length is even.
Print each word on a new line
'''

def even_length(text):
    final_list = [t for t in text.split(" ") if len(t) % 2 ==0]
    return final_list

for e in even_length(input()):
    print(e)
