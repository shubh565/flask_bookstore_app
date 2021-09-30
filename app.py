from models.book import Book
from flask import Flask
from flask import render_template, request
from book_store import BookStore


app = Flask(__name__)
book_store = BookStore()


@app.route("/")
def index():
    return render_template("index.html", books=book_store.books)


@app.route("/books")
def books_page():
    return render_template("books.html", books=book_store.books)


@app.route("/books/<int:id>")
def book_details_page(id):
    book = next((book for book in book_store.books if book.id == id), None)
    return render_template("book_details.html", book=book)


@app.route("/books/delete/<int:id>", methods=["GET", "POST"])
def book_delete(id):
    if request.method == "POST":
        book_store.delete_book(id, book_store.books)
    return render_template("books.html", books=book_store.books)


@app.route("/books/form", methods=["GET", "POST"])
def add_book_form():
    if request.method == "POST":
        book_store.add_new_book(
            Book(
                request.form["name"],
                request.form["description"],
                request.form["author"],
            )
        )
    return render_template("form.html")


@app.route("/books/edit_form/<int:id>", methods=["GET", "POST"])
def edit_book_form(id):
    # shows the form with pre-filled book deatils of given book id
    if request.method == "POST":
        book = next((book for book in book_store.books if book.id == id), None)
    return render_template("edit_form.html", book=book)


@app.route("/books/edit_form/deatils/<int:id>", methods=["GET", "POST"])
def update_book_details(id):
    # used to capture the update book details and add to list of books
    book = next((book for book in book_store.books if book.id == id), None)
    book.name = request.form.get("name")
    book.description = request.form.get("description")
    book.author = request.form.get("author")
    return render_template("books.html", books=book_store.books)
