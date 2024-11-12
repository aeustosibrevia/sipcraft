from app import app, db, Item

def delete_all_items():
    """Видаляє всі товари з БД"""
    with app.app_context():
        items = Item.query.all()
        if items:
            for item in items:
                db.session.delete(item)
            db.session.commit()
            print("Усі товари видалені")
        else:
            print("Товари не знайдено.")

if __name__ == '__main__':
    delete_all_items()
