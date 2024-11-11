from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    items = db.relationship('Item', backref='category', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    isActive = db.Column(db.Boolean, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return  self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('aboutus.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/signup')
def signup():
    return render_template('singup.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/whiskey')
def whiskey():
    items = Item.query.all()
    return render_template('whiskey.html', data=items)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
