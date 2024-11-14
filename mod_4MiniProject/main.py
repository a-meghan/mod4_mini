import book_menu
import user_menu
import author_menu

def main_menu():
    while True:
        print("Welcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        main_choice = input("Enter your choice: ")

        if main_choice == "1":
            book_operations_menu()
        elif main_choice == "2":
            user_operations_menu()
        elif main_choice == "3":
            author_operations_menu()
        elif main_choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def book_operations_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

    book_op_choice = input("Enter your choice: ")
    if book_op_choice == "1":
        book_menu.add_book_menu()
    elif book_op_choice == "2":
        book_menu.borrow_book_menu(user_menu.users)
    elif book_op_choice == "3":
        book_menu.return_book_menu(user_menu.users)
    elif book_op_choice == "4":
        book_menu.search_book_menu()
    elif book_op_choice == "5":
        book_menu.display_all_books_menu()
    else:
        print("Invalid choice. Please try again.")
        book_operations_menu()


def user_operations_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

    user_op_choice = input("Enter your choice: ")

    if user_op_choice == "1":
        user_menu.add_user_menu()
    elif user_op_choice == "2":
        user_menu.view_user_details_menu()
    elif user_op_choice == "3":
        user_menu.display_all_users_menu()
    else:
        print("Invalid choice. Please try again.")
        user_operations_menu()


def author_operations_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
  
    author_op_choice = input("Enter your choice: ")

    if author_op_choice == "1":
        author_menu.add_author_menu()
    elif author_op_choice == "2":
        author_menu.view_author_details_menu()
    elif author_op_choice == "3":
        author_menu.display_all_authors_menu()
    else:
        print("Invalid choice. Please try again.")
        author_operations_menu()

if __name__ == "__main__":  
    main_menu()