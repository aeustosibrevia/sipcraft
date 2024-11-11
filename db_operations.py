from app import app, db, Item

def delete_item(item_name):
    """Удаляет товар по имени из базы данных."""
    with app.app_context():

        item = Item.query.filter_by(name=item_name).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            print(f"Товар '{item_name}' успешно удалён.")
        else:
            print(f"Товар '{item_name}' не найден.")

if __name__ == '__main__':
    delete_item('Jack Daniel`s Old')
