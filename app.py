from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)


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


if __name__ == '__main__':
    app.run(debug=True)
