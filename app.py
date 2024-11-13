from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
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
    geography = db.Column(db.String(80), nullable=False)
    strength = db.Column(db.Float, nullable=False)
    producer = db.Column(db.String(80), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.Text, nullable=False)
    isAdmin = db.Column(db.Boolean, default=False, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('aboutus.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form['new_username']
        password = request.form['new_password']
        email = request.form['email']
        confirm_password = request.form['confirm_password']

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already taken', 'error')
            return redirect(url_for('signup'))

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('signup'))


        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('You are now registered', 'success')
        return redirect(url_for('login'))

    return render_template('singup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('You are now logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))

@app.route('/category')  # category == beer
def category():
    beer_category = Category.query.filter_by(name='Пиво').first()
    if beer_category:
        items = Item.query.filter_by(category=beer_category).all()
    else:
        items = []
    return render_template('category.html', data=items)


@app.route('/whiskey')
def whiskey():
    whiskey_category = Category.query.filter_by(name='Віскі').first()
    if whiskey_category:
        items = Item.query.filter_by(category=whiskey_category).all()
    else:
        items = []
    return render_template('whiskey.html', data=items)


@app.route('/cognac')
def cognac():
    cognac_category = Category.query.filter_by(name='Коньяк').first()
    if cognac_category:
        items = Item.query.filter_by(category=cognac_category).all()
    else:
        items = []
    return render_template('cognac.html', data=items)

@app.route('/gin')
def gin():
    gin_category = Category.query.filter_by(name='Джин').first()
    if gin_category:
        items = Item.query.filter_by(category=gin_category).all()
    else:
        items = []
    return render_template('gin.html', data=items)

@app.route('/wine')
def wine():
    wine_category = Category.query.filter_by(name='Вино').first()
    if wine_category:
        items = Item.query.filter_by(category=wine_category).all()
    else:
        items = []
    return render_template('wine.html', data=items)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
