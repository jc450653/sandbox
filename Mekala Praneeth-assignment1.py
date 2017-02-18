__author__ = 'jc450653'

# Initialize the constants

FILE = "books.csv"


def main():
    books = []
    print("Reading List 1.0 - by MEKALA PRANEETH")
    load_books(books)
    print(books)
    display_menu()
    ch = input(">>>")
    while ch.lower() != 'q':
        if ch.lower() == 'r':
            books_required_to_display(books)
        elif ch.lower() == 'c':
            books_completed_to_display(books)
        elif ch.lower() == 'a':
            books = add_books()
        elif ch.lower() == 'm':
            complete_a_book(books)
        display_menu()
        ch = input(">>>")
    print("{} books have been saved to {}".format(len(books), FILE))
    print("Have a nice day :)")


def display_menu():
    """
    This function is used to display the options Menu
"""
    menu = "Menu: \nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"
    print(menu)


# end of display_menu function

def load_books(books):
    """
    filebook <- open(FILE, 'r')
    for line in filebook:
        books.append(line.strip().split(','))
    ENDFOR
    CLOSE filebook
"""
    filebook = open(FILE, 'r')
    for line in filebook:
        books.append(line.strip().split(','))
    filebook.close()


# end of load_books()

def complete_a_book(books):
    """
    books_required_to_display(books)
    OUTPUT "Enter the number of a book to mark as completed"
    check =0
    while check = 0:
        try:
            numofbook <- int(input(">>>"))
            IF books[numofbook][3] = 'c':
                OUTPUT "That book is already completed"
            ELSE:
                books[numofbook][3] <- 'c'
                filebook <- open(FILE, 'w')
                for i in books:
                    for j in i:
                        IF j = "r" OR j = "c":
                            OUTPUT j, end='', file=filebook
                        ELSE:
                            OUTPUT j, end=',', file=filebook
                        ENDIF
                    ENDFOR
                    OUTPUT file=filebook
                END FOR
                filebook.close()
                OUTPUT title "by" author "is completed"
            END IF ELSE
            check=1
        except ValueError:
            OUTPUT "Invalid input; enter a valid number"
            complete_a_book(books)
    END WHILE
"""
    books_required_to_display(books)
    print("Enter the number of a book to mark as completed")
    check =0
    while check == 0:
        try:
            num_of_book = int(input(">>>"))
            if books[num_of_book][3] == 'c':
                print("That book is already completed")
            else:
                books[num_of_book][3] = 'c'
                filebook = open(FILE, 'w')
                for i in books:
                    for j in i:
                        if j == "r" or j == "c":
                            print(j, end='', file=filebook)
                        else:
                            print(j, end=',', file=filebook)
                    print(file=filebook)
                filebook.close()
                print("{} by {} is completed".format(books[num_of_book][0], books[num_of_book][1]))
            check=1
        except ValueError:
            print("Invalid input; enter a valid number")
            complete_a_book(books)


# end of complete_a_book()

def books_required_to_display(books):
    """
    to display required books
"""
    total = 0
    print("Required Books:")
    count1 = 0
    count2 =0
    for i in books:
        if 'r' in books[count1][3]:
            print("{}. {:<45s} by {:<15s} {:>10s} pages".format(count1, books[count1][0], books[count1][1],
                                                                books[count1][2]))
            total= total+ int(books[count1][2])
            count2= count2+ 1
        count1 += 1
    if count2 ==0:
        print("No required books")
    else:
        print("Total pages for {} books: {}".format(count1 - 1, total))


# end of books_required_to_display function

def books_completed_to_display(books):
    """
    to display completed books
"""
    total = 0
    print("Completed books:")
    count = 0
    for i in books:
        if 'c' in books[count][3]:
            print("{}. {:<45s} by {:<15s} {:>10s} pages".format(count, books[count][0], books[count][1],
                                                                books[count][2]))
            total += int(books[count][2])
        count += 1
    print("Total pages for {} books: {}".format(count + 1, total))


# end of books_completed_to_display function

def add_books():
    """
    to add new book
"""
    title_name = input("Title:")
    while title_name == "":
        print("Input can not be blank")
        title_name = input("Title:")
    author_name = input("Author:")
    while author_name == "":
        print("Input can not be blank")
        author_name = input("Author:")
    check = 0
    num_of_pages = 0
    while check == 0:
        try:
            num_of_pages = int(input("Pages: "))
            while num_of_pages <= 0:
                print("Number must be >= 0")
                num_of_pages = int(input("Pages: "))
            check = 1
        except ValueError:
            print("Invalid input; enter a valid number")
    print("{} by {}, ({} num_of_pages) added to reading list".format(title_name, author_name, num_of_pages))
    book = [title_name, author_name, str(num_of_pages), 'r']
    books = []
    load_books(books)
    books.append(book)
    print(books)
    filebook = open(FILE, 'w')
    for i in books:
        for j in i:
            if j == "r" or j == "c":
                print(j, end='', file=filebook)
            else:
                print(j, end=',', file=filebook)
        print(file=filebook)
    filebook.close()
    return books

# end of add_books function
main()
