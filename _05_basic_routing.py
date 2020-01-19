from flask import Flask
from flask import render_template
app = Flask(__name__)

BOOKS_INFO = {
    'mindset': {
        'full_name': 'Mindset - Updated Edition: Changing The Way You Think To Fulfil Your Potential',
        'author': 'Carol Dweck',
        'published': 'January 17, 2017',
        'picture': 'https://images-na.ssl-images-amazon.com/images/I/81u%2BjLjLHgL.jpg'
    },
    'habits': {
        'full_name': 'Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones',
        'author': 'James Clear',
        'published': 'October 16, 2018',
        'picture': 'https://static.raru.co.za/cover/2018/05/25/6665445-l.jpg'
    },
    'compound-effect': {
        'full_name': 'The Compound Effect',
        'author': 'Darren Hardy',
        'published': 'June 1, 2010',
        'picture':
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfk1Tg4iYiKeqEuxhgED5LGy9VWwE4C0VxlHn9XwK4kN2q4l2I'
    }
}
@app.route('/')
def library():
    books_list = []
    for book in BOOKS_INFO:

        books_list.append(book)
    print(books_list)
    return render_template('routing/books.html',
                           books=books_list)

@app.route('/book/<name_of_book>')
def book(name_of_book):
    print(BOOKS_INFO[name_of_book])
    return render_template('routing/book.html',
                           book=BOOKS_INFO[name_of_book])