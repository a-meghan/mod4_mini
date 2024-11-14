import author  

authors = {}

def add_author_menu():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    author_obj = author.Author(name, biography)
    authors[name] = author_obj
    print("Author added successfully!")

def view_author_details_menu():
    author_name = input("Enter author name: ")
    if author_name in authors:
        author_obj = authors[author_name]
        print("Author details:")
        print("Name:", author_obj.get_name())
        print("Biography:", author_obj.get_biography())
    else:
        print("Author not found.")

def display_all_authors_menu():
    print("All authors:")
    for author_name, author_obj in authors.items():
        print("Name:", author_obj.get_name())
        print("Biography:", author_obj.get_biography())