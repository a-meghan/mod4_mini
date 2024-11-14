class Book:  
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability_status = "Available"

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def get_publication_date(self):
        return self.publication_date

    def get_availability_status(self):
        return self.availability_status

    def set_availability_status(self, status):
        self.availability_status = status
