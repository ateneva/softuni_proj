
'''
Create a class called Book.
It should have an __init__() method that should receive:
•	name : string
•	author : string
•	pages : int
'''

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)


# OR

# for python 3.7 +
from dataclasses import dataclass

@dataclass
class Books:
    name: str
    author: str
    pages: int

book = Books("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
