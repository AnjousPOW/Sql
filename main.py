from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'RHRWhrwhRSWHRWsh34'
db.init_app(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', backref='author', lazy=True)

    def __init__(self, name):
        self.name = name


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', backref='genre', lazy=True)

    def __init__(self, name):
        self.name = name




class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    price = db.Column(db.Float(50))
    amount = db.Column(db.Float(50))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'),
                          nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'),
                         nullable=False)

    def __init__(self, title, author, genre, price, amount):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.amount = amount


with app.app_context():
    db.create_all()

    a1 = Author(u'Булгаков М.А.')
    a2 = Author(u'Достоевский Ф.М.')
    a3 = Author(u'Есенин С.А.')
    a4 = Author(u'Пастернак Б.Л.')
    a5 = Author(u'Лермонтов М.Ю.')


    j1 = Genre(u'Роман')
    j2 = Genre(u'Поэзия')
    j3 = Genre(u'Приключения')

    db.session.add(Book('Мастер и Маргарита', a1, j1, 670.99, 3))
    db.session.add(Book('Белая гвардия', a1, j1, 540.50, 5))
    db.session.add(Book('Идиот', a2, j1, 460.00, 10))
    db.session.add(Book('Братья Карамазовы', a2, j1, 799.01, 3))
    db.session.add(Book('Игрок', a2, j1, 480.50, 10))
    db.session.add(Book('Стихотворения и поэмы', a3, j2, 650.00, 15))
    db.session.add(Book('Черный человек', a3, j2, 570.20, 6))
    db.session.add(Book('Лирика', a4, j2, 518.99, 2))

    db.session.commit()

@app.route('/base', methods=['GET', 'POST'])
def add_user():
    Book = Book()
    if request.method == 'POST':
        author_name = request.form.get('author_name')
        curAuthor = Author.query.filter_by(name=author_name).first()
        Author.query.filter(Author.title.endswith(author_name)).all()

        return render_template('base.html', author=curAuthor)

    return render_template('base.html')


app.run()





