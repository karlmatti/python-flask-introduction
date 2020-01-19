from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def library():
    library_name = "Self-development"

    books = ["Mindset", "Atomic Habits", "Compound effect"]

    return render_template('index.html', name=library_name, books=books)
