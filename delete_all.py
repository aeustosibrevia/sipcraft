from app import app, db, Item, CartItem

def delete_all_items():
    """Видаляє всі товари з БД разом із залежностями"""
    with app.app_context():
        items = Item.query.all()
        if items:
            for item in items:
                db.session.query(CartItem).filter_by(item_id=item.id).delete()
                db.session.delete(item)
            db.session.commit()
            print("Усі товари видалені")
        else:
            print("Товари не знайдено.")

if __name__ == '__main__':
    delete_all_items()