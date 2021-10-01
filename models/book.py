class Book:
    def __init__(self, name, description, author):
        self.id = 0
        self.name = name
        self.description = description
        self.author = author

    def update(self, book):
        self.name = book.name or self.name
        self.description = book.description or self.description
        self.author = book.author or self.author
