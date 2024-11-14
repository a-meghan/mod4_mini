import user
  
users = {}

def add_user_menu():
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    user_obj = user.User(name, library_id)
    users[library_id] = user_obj
    print("User added successfully!")

def view_user_details_menu():
    user_id = input("Enter user ID: ")
    if user_id in users:
        user_obj = users[user_id]
        print("User details:")
        print("Name:", user_obj.get_name())
        print("Library ID:", user_obj.get_library_id())
        print("Borrowed books:", user_obj.get_borrowed_books())
    else:
        print("User not found.")

def display_all_users_menu():
    print("All users:")
    for user_id, user_obj in users.items():
        print("Name:", user_obj.get_name())
        print("Library ID:", user_obj.get_library_id())
        print("Borrowed books:", user_obj.get_borrowed_books())