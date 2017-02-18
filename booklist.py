# create your BookList class in this file
BOOK_FILE = "books.csv"
from book import *


class BookList(object):
    book_list = []

    def __int__(self):
        self.book_list = []

    def __str__(self):
        temp_list = []
        for book in self.book_list:
            temp_list.append([str(book)])
        return str(temp_list)

    def add_book(self, title, author, pages):
        b = Book(title, author, pages)
        self.book_list.append(b)

    def get_book_by_title(self, title):
        for book in self.book_list:
            if book.book_title == title:
                return book

    def get_total(self, status='r'):
        total = 0
        for book in self.book_list:
            if book.status == status:
                total += int(book.num_pages)
        return total

    def load_books(self):
        book_file = open(BOOK_FILE, 'r')
        for line in book_file:
            temp_book_list = line.strip().split(',')
            book = Book(temp_book_list[0], temp_book_list[1], temp_book_list[2], temp_book_list[3])
            self.book_list.append(book)
        book_file.close()
        if len(self.book_list) == 0:
            print('No books.')
        else:
            print("{} books loaded from {}".format(len(self.book_list), BOOK_FILE))

    def save_books(self):
        book_file = open(BOOK_FILE, 'w')
        print(self.book_list)
        for book in self.book_list:
            book_line = book.book_title + ',' + book.author_name + ',' + str(book.num_pages) + ',' + book.status
            print(book_line, file=book_file)
        book_file.close()
        print('Saved!')
