from models.book import Book
from flask import Flask
from flask import render_template, request, url_for, redirect
from book_store import BookStore


app = Flask(__name__)
book_store = BookStore()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books_page():
    return render_template("books/books.html", books=book_store.books)


@app.route("/books/<int:id>")
def book_details_page(id):
    book = next((book for book in book_store.books if book.id == id), None)
    if not book:
        return redirect(url_for("books_page"))

    return render_template("books/book_details.html", book=book)


@app.route("/books/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book_store.add_new_book(
            Book(
                request.form["name"],
                request.form["description"],
                request.form["author"],
            )
        )
        return redirect(url_for("books_page"))
    return render_template("books/add_book.html")


@app.route("/books/delete/<int:id>", methods=["POST"])
def delete_book(id):
    book_store.delete_book(id, book_store.books)
    return redirect(url_for("books_page"))


@app.route("/books/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id):
    if request.method == "POST":
        book_store.edit_book(
            id,
            Book(
                request.form["name"],
                request.form["description"],
                request.form["author"],
            ),
        )
        print(book_store.books)
        return redirect(url_for("books_page"))

    book = next((book for book in book_store.books if book.id == id), None)
    return render_template("books/edit_book.html", book=book)
