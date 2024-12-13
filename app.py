from flask import Flask, render_template, flash, redirect, url_for, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from werkzeug.utils import secure_filename
from datetime import timedelta

#  пофіксити візуал з flash повідомленнями, всі відображення перекласти українською
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
db = SQLAlchemy(app)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
    isActive = db.Column(db.Boolean, nullable=False, default=True)
    quantity = db.Column(db.Integer, nullable=False, default=10)
    geography = db.Column(db.String(80), nullable=False)
    strength = db.Column(db.Float, nullable=False)
    producer = db.Column(db.String(80), nullable=False)
    volume = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    second_name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    item = db.relationship('Item', backref='cart_items', lazy=True)

class FavoriteItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    user = db.relationship('User', backref='favorites', lazy=True)
    item = db.relationship('Item', lazy=True)



@app.route('/')
def index():
    is_admin = session.get('isAdmin', False)
    #print(f"Is Admin {is_admin}")
    return render_template('index.html', is_admin=is_admin)


def check_liked_items(items):
    liked_items_set = set()
    if 'user_id' in session:
        user_id = session['user_id']
        liked_items_set = {
            favorite.item_id for favorite in FavoriteItem.query.filter_by(user_id=user_id).all()
        }

    data = []
    for item in items:
        data.append({
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'image_url': item.image_url,
            'is_liked': item.id in liked_items_set
        })

    return data

@app.route('/about')
def about():
    return render_template('aboutus.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category_id = request.form.get('category_id')
        volume = request.form.get('volume')
        geography = request.form.get('geography')
        strength = request.form.get('strength')
        producer = request.form.get('producer')
        description = request.form.get('description')

        file = request.files.get('image')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            image_url = filepath
        else:
            image_url = None

        item = Item(
            name=name,
            price=price,
            category_id=category_id,
            volume=volume,
            geography=geography,
            strength=strength,
            producer=producer,
            description=description,
            image_url=image_url
        )
        db.session.add(item)
        db.session.commit()
        return render_template('admin.html', item=item)
    else:
        return render_template('admin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        first_name = request.form['new_first_name']
        second_name = request.form['new_second_name']
        phone_number = request.form['new_phone_number']
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

        new_user = User(username=username, email=email, first_name=first_name, second_name=second_name, phone_number=phone_number)
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
            session['isAdmin'] = user.isAdmin
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
    session.pop('isAdmin', None)
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))

@app.route('/api/auth_status', methods=['GET'])
def auth_status():
    is_logged_in = 'user_id' in session
    username = session.get('username', '') if is_logged_in else ''
    is_admin = session.get('isAdmin', False)
    return jsonify({'isLoggedIn': is_logged_in, 'username': username, 'isAdmin': is_admin})


@app.route('/category')  # category == beer
def category():
    is_admin = session.get('isAdmin', False)
    beer_category = Category.query.filter_by(name='Пиво').first()
    if beer_category:
        items = Item.query.filter_by(category=beer_category).all()
    else:
        items = []

    data = check_liked_items(items)
    return render_template('category.html', data=data, is_admin=is_admin)


@app.route('/whiskey')
def whiskey():
    whiskey_category = Category.query.filter_by(name='Віскі').first()
    if whiskey_category:
        items = Item.query.filter_by(category=whiskey_category).all()
    else:
        items = []

    data = check_liked_items(items)

    return render_template('whiskey.html', data=data)



@app.route('/cognac')
def cognac():
    cognac_category = Category.query.filter_by(name='Коньяк').first()
    if cognac_category:
        items = Item.query.filter_by(category=cognac_category).all()
    else:
        items = []

    data = check_liked_items(items)
    return render_template('cognac.html', data=data)


@app.route('/gin')
def gin():
    gin_category = Category.query.filter_by(name='Джин').first()
    if gin_category:
        items = Item.query.filter_by(category=gin_category).all()
    else:
        items = []

    data = check_liked_items(items)
    return render_template('gin.html', data=data)


@app.route('/wine')
def wine():
    wine_category = Category.query.filter_by(name='Вино').first()
    if wine_category:
        items = Item.query.filter_by(category=wine_category).all()
    else:
        items = []

    data = check_liked_items(items)
    return render_template('wine.html', data=data)


@app.route('/add_to_cart/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'Будь ласка, увійдіть, аби додавати товари до кошика.'}), 401

    user_id = session['user_id']

    if request.is_json:
        data = request.get_json()
        quantity = data.get('quantity', 1)
    else:
        try:
            quantity = int(request.form.get('quantity', 1))
        except ValueError:
            return jsonify({'status': 'error', 'message': 'Неправильна кількість. Спробуйте ще раз.'}), 400

    if quantity < 1:
        return jsonify({'status': 'error', 'message': 'Неправильна кількість. Неможливо додати до кошика.'}), 400

    cart_item = CartItem.query.filter_by(user_id=user_id, item_id=item_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(user_id=user_id, item_id=item_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Товар успішно додано до кошика'}), 200



@app.route('/cart')
def cart():
    user_id = session.get('user_id')

    if not user_id:
        flash('Please log in to view your cart.', 'error')
        return redirect(url_for('login'))

    cart_items = CartItem.query.filter_by(user_id=user_id).all()

    total_price = sum(item.item.price * item.quantity for item in cart_items)

    return render_template(
        'cart.html',
        data=cart_items,
        total_price=total_price
    )


@app.route('/update_quantity', methods=['POST'])
def update_quantity():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    action = data.get('action')
    item_id = data.get('item_id')

    if not item_id or action not in ['increase', 'decrease']:
        return jsonify({'error': 'Invalid data'}), 400

    user_id = session['user_id']
    cart_item = CartItem.query.filter_by(user_id=user_id, item_id=item_id).first()

    if not cart_item:
        return jsonify({'error': 'Item not found in cart'}), 404

    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    else:
        db.session.delete(cart_item)

    db.session.commit()
    return jsonify({'success': True})


@app.route('/remove_from_cart', methods=['POST', 'GET'])
def remove_from_cart():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    item_id = data.get('item_id')

    if not item_id:
        return jsonify({'error': 'Invalid data'}), 400

    user_id = session['user_id']
    cart_item = CartItem.query.filter_by(user_id=user_id, item_id=item_id).first()

    if not cart_item:
        return jsonify({'error': 'Item not found in cart'}), 404

    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({'success': True})


@app.route('/product/<int:item_id>', methods=['GET', 'POST'])
def item_page(item_id):
    item = Item.query.get(item_id)
    if not item:
        return render_template('404.html'), 404

    is_liked = False
    if 'user_id' in session:
        user_id = session['user_id']
        is_liked = FavoriteItem.query.filter_by(user_id=user_id, item_id=item.id).first() is not None

    return render_template('product.html', item=item, is_liked=is_liked)




@app.route('/add_to_liked/<int:item_id>', methods=['POST'])
def liked_item(item_id):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Будь ласка, увійдіть, щоб додавати товари в список бажаного.'}), 403

    user_id = session['user_id']

    favorite_item = FavoriteItem.query.filter_by(user_id=user_id, item_id=item_id).first()
    if favorite_item:
        db.session.delete(favorite_item)
        db.session.commit()
        return jsonify({'success': True, 'liked': False})
    else:
        favorite_item = FavoriteItem(user_id=user_id, item_id=item_id)
        db.session.add(favorite_item)
        db.session.commit()
        return jsonify({'success': True, 'liked': True})



@app.route('/liked')
def liked():
    user_id = session.get('user_id')

    if not user_id:
        flash('Please log in to view your favorites.', 'error')
        return redirect(url_for('login'))

    liked_items = FavoriteItem.query.filter_by(user_id=user_id).all()

    return render_template(
        'liked.html',
        data=liked_items
    )


@app.route('/remove_from_liked/<int:item_id>', methods=['POST'])
def remove_from_liked(item_id):
    if 'user_id' not in session:
        flash('Будь ласка, увійдіть у свій акаунт, щоб видалити товар зі списку бажань.', 'error')
        return redirect(url_for('login'))

    user_id = session['user_id']

    liked_item = FavoriteItem.query.filter_by(user_id=user_id, item_id=item_id).first()

    if not liked_item:
        flash('Товар не знайдено у списку бажань.', 'error')
        return redirect(url_for('liked'))

    db.session.delete(liked_item)
    db.session.commit()

    flash('Товар успішно видалено зі списку бажань.', 'success')
    return redirect(url_for('liked'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()
    if query:
        results = Item.query.filter(
            Item.isActive == True,
            (Item.name.ilike(f'%{query}%') |
             Item.description.ilike(f'%{query}%') |
             Item.producer.ilike(f'%{query}%'))
        ).all()
    else:
        results = []
    return render_template('search_results.html', results=results, query=query)


@app.route('/search_product', methods=['GET'])
def search_product():
    query = request.args.get('q', '').strip()
    if not query:
        return redirect(url_for('search_product'))
    product = Item.query.filter(Item.name.ilike(f'%{query}%')).all()
    return render_template('admin.html', product=product)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
