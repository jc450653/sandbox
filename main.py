"""
Name: Praneeth
Date: 30/01/2017
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from booklist import *


class ReadingListApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.books = BookList()
        self.books.load_books()

    def build(self):
        self.title = "Reading List 2.0"
        self.root = Builder.load_file('app.kv')
        self.list_required_books()
        return self.root

    def main(self):
        self.books.save_books()

    def add_book(self, title='', author='', pages=''):
        self.books.add_book(title, author, pages)

    def list_required_books(self):
        self.root.ids.middle_layout.clear_widgets()
        count = 0
        num_books = 0
        for book in self.books.book_list:
            if 'r' in book.status:
                temp_button = Button(text=book.book_title)
                temp_button.bind(on_release=self.mark_book_completed)
                self.root.ids.middle_layout.add_widget(temp_button)
                num_books += 1
            count += 1
        total = self.books.get_total()
        if num_books > 0:
            print("Total pages for {} books: {}".format(count - 1, total))
            self.root.ids.top_layout.text = "Total pages to read: " + str(total)
            self.root.ids.bottom_layout.text = "Clicks Books to mark them as complete"
        else:
            print("No books")
            self.root.ids.top_layout.text = "Total pages to read: " + str(total)
            self.root.ids.bottom_layout.text = "All book are completed"

    def mark_book_completed(self, instance):
        title = instance.text
        book = self.books.get_book_by_title(title)
        book.mark_a_book_completed()
        self.list_required_books()
        self.root.ids.bottom_layout.text = title + " is marked as completed"
        print(self.books.book_list)

    def list_completed_books(self):
        self.root.ids.middle_layout.clear_widgets()
        count = 0
        num_books = 0
        for book in self.books.book_list:
            if 'c' in book.status:
                temp_button = Button(text=book.book_title)
                temp_button.bind(on_release=self.status_completed_books)
                self.root.ids.middle_layout.add_widget(temp_button)
                num_books += 1
            count += 1
        total = self.books.get_total('c')
        if num_books > 0:
            self.root.ids.top_layout.text = "Total pages completed: " + str(total)
            self.root.ids.bottom_layout.text = "Click the book to see details"
        else:
            self.root.ids.bottom_layout.text = "No Book is completed to display"

    def clear_view(self):
        self.root.ids.title.text = ''
        self.root.ids.author.text = ''
        self.root.ids.pages.text = ''

    def status_completed_books(self, instance):
        title = instance.text
        book = self.books.get_book_by_title(title)
        self.root.ids.bottom_layout.text = book.title + " by " + book.author + ", " + book.pages + " (Completed)"


application = ReadingListApp()
application.run()
application.main()
