# create your simple Book class in this file

class Book(object):
    def __init__(self, book_title='', author_name='', num_pages=0, status='r'):
        self.book_title = book_title
        self.author_name = author_name
        self.num_pages = num_pages
        self.status = status

    def __str__(self):
        return self.book_title + ',' + self.author_name + ',' + str(self.num_pages) + ',' + self.status

    def mark_a_book_completed(self):
        self.status = 'c'

    def is_long_book(self):
        return int(self.num_pages) >= 500
