from app import app, db, Item

def delete_item(item_name):
    """Видаляє товар по імені із БД"""
    with app.app_context():

        item = Item.query.filter_by(name=item_name).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            print(f"Товар '{item_name}' видалено")
        else:
            print(f"Товар '{item_name}' не знайдено.")

if __name__ == '__main__':
    delete_item('Jack Daniel`s Old')
