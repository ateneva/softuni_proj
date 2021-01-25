
# -----------------------08. loading bar (exam problem)-------------------------

'''
You will receive a single integer number between 0 and 100
    which is divided with 10 without residue (0, 10, 20, 30...).

Your task is to create a function that visualizes a loading bar depending on
    the number you have received in the input.
'''

# --------------100 points --------------------
x = int(input())

def progress_bar(x):
    progress = int(x/10) * '%'
    bar = int(10 - (x/10)) * '.'

    if x > 0 and x < 100:
        result = f'{x}% ' + '[' + progress + bar + ']' + '\n' + 'Still loading...'
    else:
        result = '100% Complete!' + '\n' + '[' + progress + bar + ']'

    return result

print(progress_bar(x))
