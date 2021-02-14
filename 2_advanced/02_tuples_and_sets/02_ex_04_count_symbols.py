
# ---------------------problem 4: coutn occurences-----------------------------

'''
Write a program that reads a text from the console and counts the
occurrences of each character in it.
Print the results in alphabetical (lexicographical) order.
'''

def count_symbols(text):
    for t in sorted(set(text)):
        times = text.count(t)
        print(f'{t}: {times} time/s')

count_symbols(input())
