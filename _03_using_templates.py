from flask import Flask
from flask import render_template_string

app = Flask(__name__)


@app.route('/')
def library():
    library_name = "Self-development"
    html = """
        <html>
            <h1>Welcome to the {{name}} library!</h1>
            <ul>
                {% for book in books %}
                <li>{{ book }}</li>
                {% endfor %}
            </ul>
        </html>
    """

    books = ["Mindset", "Atomic Habits", "Compound effect"]
    rendered_html = render_template_string(html, name=library_name, books=books)

    return rendered_html
