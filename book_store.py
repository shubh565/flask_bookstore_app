from models.book import Book


class BookStore:
    def __init__(self):
        self.books = []
        self.last_book_id = 0
        self.generate_demo_data()

    def add_new_book(self, book):
        book.id = self.last_book_id + 1
        self.books.append(book)
        self.last_book_id += 1

    def edit_book(self, id, modified_book):
        for book in self.books:
            if book.id == id:
                book.update(modified_book)
                return

    def delete_book(self, id, books):
        for book in books:
            if book.id == id:
                books.remove(book)

    def generate_demo_data(self):
        data = [
            {
                "name": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "description": "Humour entwines the delicate strands of prejudice",
            },
            {
                "name": "1984",
                "author": "George Orwell",
                "description": "totalitarian world of control, fear and lies",
            },
            {
                "name": "Harry Potter and the Philosopher’s Stone",
                "author": "J.K. Rowling",
                "description": "journey into the world of magic",
            },
            {
                "name": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "description": "expansive fantasy world filled with turmoil, heroes, evil",
            },
            {
                "name": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "the decadence of the Jazz Age, and one man’s introduction into a world",
            },
        ]
        for book in data:
            self.add_new_book(Book(book["name"], book["description"], book["author"]))
