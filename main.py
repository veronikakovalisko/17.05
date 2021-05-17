"""
Task 2
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) -
returns an instance of Book class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
```
class Library:
    pass
class Book:
    pass
class Author:
    pass
```
"""
class Book:
    name_of_book = ''
    year = ''
    author = ''
    def __init__(self, name, year, author):
        self.name_of_book = name
        self.year = year
        self.author = author

class Author:
    name_of_author = ''
    country = ''
    birthday = 1111
    books = []
    def __init__(self, name, country, birthday, books):
        self.name_of_author = name
        self.birthday = birthday
        self.country = country
        self.books = books

class Library(Book, Author):
    name_of_library = ''
    books = []
    authors = []
    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author: Author):
        for i in self.books:
            if i.author == author.name_of_author:
                return i.name_of_book

    def group_by_year(self, year: int):
        for i in self.books:
            if i.year == year:
                return i.name_of_book

if __name__ == '__main__':
    book = Book('harry potter', 2009, 'rowling')
    b = Library
    b2 = Library
    a1 = Author('rowling', 'uk', 1111, 'harry potter')
    a2 = Author('tolkien', 'usa', 1111, 'lord of rings')
    b.new_book(b, 'harry potter', 2008, a1.name_of_author)
    b2.new_book(b2, 'lord of rings', 2009, a2.name_of_author)
    l = Library
    l.books
    print(l.group_by_author(l, a2))
    print(l.group_by_year(l, 2008))
"""
Task 3
Fraction
Create a Fraction class, which will represent all basic arithmetic logic 
for fractions (+, -, /, *) with appropriate checking and error handling
```
class Fraction:
pass
x = Fraction(1/2)
y = Fraction(1/4)
x + y == Fraction(3/4)
```
"""
class Fraction:
    zn = 1
    chs = 1
    def drib (self):
        return f"{self.zn}/{self.chs}"

    def zl_ch(self):
        if self.zn // self.chs == 0:
            return self.zn / self.chs
        elif self.zn // self.chs > 0:
            return f"{self.zn // self.chs}*{self.zn // self.chs}/{self.chs}"
    def dod(self, zn, chs, zn2, chs2):
        self.chs = chs
        self.zn = zn
        self.chs2 = chs2
        self.zn2 = zn2
        if self.chs == self.chs2:
            self.zn = self.zn + self.zn2
            return f"{self.zn}/{self.chs}"
        else:
            self.chs = self.chs2 = nsk(chs, chs2)
            self.zn *= self.chs/chs
            self.zn2 *= self.chs2/chs2
            self.zn = self.zn + self.zn2
            return f"{self.zn}/{self.chs}"
    def mn(self, zn, chs, zn2, chs2):
        self.chs = chs*chs2
        self.zn = zn*zn2
        return f"{self.zn}/{self.chs}"
"""def zl_ch(a, b):
    if a //b == 0:
        return a / b
    elif a // b > 0:
        return f"{a // b}*{a // b}/{b}"
    else:
        return f"{a // b}/{b}"""
def nsd(a, b):
    while a*b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b
def nsk(a, b):
    nsk = a * b // nsd(a, b)
    return nsk

if __name__ == '__main__':
    z = Fraction
    print(z.mn(z, 5, 6, 3, 5))
    #print(z.skr(z))




