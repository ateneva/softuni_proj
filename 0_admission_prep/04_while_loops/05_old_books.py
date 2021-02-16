
# old books---------------------------------------------------------------------
fav_book = input()
books = int(input())
iterations = 0
isFound = False

while iterations < books:
    book = input()
    if book == fav_book:
        isFound = True
        break

    iterations +=1
    if iterations == books:
        isFound = False
        break

if isFound:
    print(f'You checked {iterations} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {iterations} books.')
