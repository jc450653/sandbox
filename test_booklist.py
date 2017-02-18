"""
(incomplete) Tests for BookList class
"""
from booklist import BookList
from book import Book

books = BookList()

# test empty BookList
print(books)
assert len(books.book_list) == 0

# test loading books
books.load_books()
print(books)
assert len(books.book_list) > 0  # assuming CSV file is not empty

books.add_book('some book', 'some author', 123)
print(books)

books.save_books()

book = books.get_book_by_title('The Practice of Computing Using Python')
print(book)

total_pages = books.get_total()
print(total_pages)