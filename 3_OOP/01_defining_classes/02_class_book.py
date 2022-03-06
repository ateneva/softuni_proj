
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


#### demo first steps in OOP
# https://softuni.bg/trainings/resources/video/69624/video-22-february-2022-ines-kenova-python-oop-february-2022/3591

class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def open(self):
        print(f'Opening the book {self.title} with author {self.author.first_name}')

    def close(self):
        pass

author = Author("Jay", "Shetty")
book = Book("My Book", author, 200)
print(book.title)
print(book.author)
print(book.pages)
print(book.author.first_name)
print(book.author.last_name)
print(book.open())