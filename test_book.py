"""
(incomplete) Tests for Book class
"""
from book import Book

# test empty book (defaults)
book = Book()
print(book)
assert book.author_name == ""
assert book.book_title == ""
assert book.num_pages == 0

# test initial-value book
book2 = Book("title", "author", 987, 'r')
print(book2)
print(book2.is_long_book())
book2.mark_a_book_completed()
print(book2)
# test mark_completed()
