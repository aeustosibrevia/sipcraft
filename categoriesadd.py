from app import db, Category, Item, app
from get_description import get_description_from_file

def add_categories_and_items():
    # Создайте категорию "Віскі"
    whiskey_category = Category(name='Віскі')
    db.session.add(whiskey_category)
    db.session.commit()

    # Добавьте несколько товаров в категорию "Віскі"
    whiskey_items = [
        {'name': 'Jack Daniel`s Old', 'price': 789, 'description_file': 'whiskey_1',
         'image_url': 'static/picture/alcohol/whiskey/jackblack.png', 'isActive': True, 'quantity': 10},
        {'name': 'Jameson', 'price': 1125, 'description_file': 'whiskey_2',
         'image_url': 'static/picture/alcohol/whiskey/jameson.png', 'isActive': True, 'quantity': 10},
        {'name': 'Jim Beam White', 'price': 1355, 'description_file': 'whiskey_3',
         'image_url': 'static/picture/alcohol/whiskey/jimbeam.png', 'isActive': True, 'quantity': 10},
        {'name': 'Woodford Reserve', 'price': 875, 'description_file': 'whiskey_4',
         'image_url': 'static/picture/alcohol/whiskey/woodford.png', 'isActive': True, 'quantity': 10},
        {'name': 'Baileys Whiskey', 'price': 80000, 'description_file': 'whiskey_5',
         'image_url': 'static/picture/alcohol/whiskey/baileysw.png', 'isActive': True, 'quantity': 10},
        {'name': 'Jack Daniel`s Tennessee Apple', 'price': 789, 'description_file': 'whiskey_6',
         'image_url': 'static/picture/alcohol/whiskey/jackapple.png', 'isActive': True, 'quantity': 10},
        {'name': 'Jack Daniel`s Tennessee Fire', 'price': 789, 'description_file': 'whiskey_7',
         'image_url': 'static/picture/alcohol/whiskey/jackfire.png', 'isActive': True, 'quantity': 10},
    ]

    for item_data in whiskey_items:
        description = get_description_from_file(item_data['description_file'])
        item = Item(
            name=item_data['name'],
            price=item_data['price'],
            description=description,
            image_url=item_data['image_url'],
            isActive=item_data['isActive'],
            quantity=item_data['quantity'],
            category=whiskey_category  # Связь с категорией
        )
        db.session.add(item)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():  # Создаем контекст приложения
        add_categories_and_items()
