
# ---------------------------------01. Disneyland Journey (Conditional Statements)-------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20191210_mid_exam_retake

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
