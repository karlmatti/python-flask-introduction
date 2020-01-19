from flask import Flask

app = Flask(__name__)


@app.route('/')
def books():
    html = """
        <html>
            <h1>Welcome to the Library!</h1>
            {books}
        </html>
    """
    books = ["Mindset", "Atomic Habits", "Compound effect"]
    book_list = "<ul>"
    book_list += "\n".join([
        "<li>{book}</li>".format(book=book) for book in books
    ])


    return html.format(books=book_list)
