class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []
  
    def get_name(self):
        return self.name

    def get_library_id(self):
        return self.library_id

    def get_borrowed_books(self):
        return self.borrowed_books

    def add_borrowed_book(self, book_title):
        self.borrowed_books.append(book_title)

    def remove_borrowed_book(self, book_title):
        self.borrowed_books.remove(book_title)