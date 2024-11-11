from app import app, db, Item

def delete_item(item_name):
    """Удаляет товар по имени из базы данных."""
    with app.app_context():
        # Найти товар по имени
        item = Item.query.filter_by(name=item_name).first()
        if item:
            db.session.delete(item)
            db.session.commit()  # Подтвердить удаление
            print(f"Товар '{item_name}' успешно удалён.")
        else:
            print(f"Товар '{item_name}' не найден.")

# Пример использования: удаление товара с именем 'Whiskey 1'
if __name__ == '__main__':
    # Вы можете указать имя товара для удаления, например:
    delete_item('Jack Daniel`s Old')
