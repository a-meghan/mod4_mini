import book  

books = {}

def add_book_menu():
    title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date: ")
    book_obj = book.Book(title, author_name, genre, publication_date)
    books[title] = book_obj
    print("Book added successfully!")

def borrow_book_menu(users):
    title = input("Enter book title: ")
    user_id = input("Enter user ID: ")
    if title in books and user_id in users:
        book_obj = books[title]
        user_obj = users[user_id]
        if book_obj.get_availability_status() == "Available":
            book_obj.set_availability_status("Borrowed")
            user_obj.add_borrowed_book(title)
            print("Book borrowed successfully!")
        else:
            print("Book is not available.")
    else:
        print("Book or user not found.")

def return_book_menu(users):
    title = input("Enter book title: ")
    user_id = input("Enter user ID: ")
    if title in books and user_id in users:
        book_obj = books[title]
        user_obj = users[user_id]
        if book_obj.get_availability_status() == "Borrowed":
            book_obj.set_availability_status("Available")
            user_obj.remove_borrowed_book(title)
            print("Book returned successfully!")
        else:
            print("Book is not borrowed.")
    else:
        print("Book or user not found.")

def search_book_menu():
    title = input("Enter book title: ")
    if title in books:
        book_obj = books[title]
        print("Book details:")
        print("Title:", book_obj.get_title())
        print("Author:", book_obj.get_author())
        print("Genre:", book_obj.get_genre())
        print("Publication Date:", book_obj.get_publication_date())
    else:
        print("Book not found.")

def display_all_books_menu():
    print("All books:")
    for title, book_obj in books.items():
        print("Title:", book_obj.get_title())
        print("Author:", book_obj.get_author())
        print("Genre:", book_obj.get_genre())
        print("Publication Date:", book_obj.get_publication_date())