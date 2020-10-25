
# ---------------------------------01. Disneyland Journey (Conditional Statements)-------------------------

# ------- 100 points -----------------------

journey_cost = float(input())
months = int(input())
saved = 0

for month in range(1, months + 1):
    if month > 1 and month % 2 != 0:
        saved -= saved*0.16

    if month % 4 == 0:
        saved += saved * 0.25

    saved += journey_cost * 0.25     # if at the end in brief; calc must be after ifs

if saved > journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {saved - journey_cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {abs(saved-journey_cost):.2f}lv. more.")

# ---------------------------------02. Archery Tournament (Lists Basic)------------------------------------

targets = list(map(int,input().split("|")))
command = input()
points = 0

while command != "Game over":
    command = command.split("@")
    do = command[0]

    #print(targets, do, command)

    if do == 'Shoot Left':
        start = int(command[1])
        length = int(command[2])
        idx = len(targets) - ((start + length) % len(targets))

        if 0 <= start < len(targets):
            targets[idx] -= 5
            points += 5

    elif do == 'Shoot Right':
        start = int(command[1])
        length = int(command[2])
        idx = (start + length) % len(targets)

        if 0 <= start < len(targets):
            targets[idx] -= 5
            points += 5

    elif do == 'Reverse':
        targets.reverse()

    command = input()

print(" - ".join(map(str,targets)))
print(f"Iskren finished the archery tournament with {points} points!")


# ---------------------------------03. School Library (Lists Advanced) -------------------------------------

# ------- 100 points -----------------------

books = input().split("&")
command = input()
#print(books)

while command != 'Done':
    do = command.split(" | ")[0]
    book = command.split(" | ")[1]

    if do == "Add Book":
        if book not in books:
            books.insert(0, book)

    elif do == "Take Book":
        if book in books:
            books.remove(book)

    elif do == "Swap Books":
        book_one = command.split(" | ")[1]
        book_two = command.split(" | ")[2]
        if book_one in books:
            if book_two in books:
                idx_one = books.index(book_one)
                idx_two = books.index(book_two)
                books[idx_one], books[idx_two] = books[idx_two], books[idx_one]

    elif do == "Insert Book":
        books.append(book)

    elif do == 'Check Book':
        idx = int(book)
        if idx < len(books):
            print(books[idx])

    #print(books, do, book)

    command = input()
print(", ".join(books))
