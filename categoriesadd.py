from app import db, Category, Item, app
from get_description import get_description_from_file

def add_categories_and_items():
    whiskey_category = Category.query.filter_by(name='Віскі').first()
    if not whiskey_category:
        whiskey_category = Category(name='Віскі')
        db.session.add(whiskey_category)
        db.session.commit()

    # Список товаров для категории "Віскі"
    whiskey_items = [
        {'name': 'Jack Daniel`s Old', 'price': 789, 'description_file': 'whiskey_1',
         'image_url': 'static/picture/alcohol/whiskey/jackblack.png', 'isActive': True,
         'quantity': 10, 'geography': 'США', 'strength': 40, 'producer': 'Jack Daniels'},
        {'name': 'Jameson', 'price': 1125, 'description_file': 'whiskey_2',
         'image_url': 'static/picture/alcohol/whiskey/jameson.png', 'isActive': True,
         'quantity': 10, 'geography': 'Ірландія', 'strength': 40, 'producer': 'Jameson' },
        {'name': 'Jim Beam White', 'price': 1355, 'description_file': 'whiskey_3',
         'image_url': 'static/picture/alcohol/whiskey/jimbeam.png', 'isActive': True,
         'quantity': 10, 'geography': 'США', 'strength': 40, 'producer': 'Jim Beam'},
        {'name': 'Woodford Reserve', 'price': 875, 'description_file': 'whiskey_4',
         'image_url': 'static/picture/alcohol/whiskey/woodford.png', 'isActive': True,
         'quantity': 10, 'geography': 'США', 'strength': 40, 'producer': 'Woodford Reserve'},
        {'name': 'Baileys Whiskey', 'price': 80000, 'description_file': 'whiskey_5',
         'image_url': 'static/picture/alcohol/whiskey/baileysw.png', 'isActive': True,
         'quantity': 10, 'geography': 'Ірландія', 'strength': 40, 'producer': 'Diageo'},
        {'name': 'Jack Daniel`s Tennessee Apple', 'price': 789, 'description_file': 'whiskey_6',
         'image_url': 'static/picture/alcohol/whiskey/jackapple.png', 'isActive': True,
         'quantity': 10, 'geography': 'США', 'strength': 35, 'producer': 'Jack Daniels'},
        {'name': 'Jack Daniel`s Tennessee Fire', 'price': 789, 'description_file': 'whiskey_7',
         'image_url': 'static/picture/alcohol/whiskey/jackfire.png', 'isActive': True,
         'quantity': 10, 'geography': 'США', 'strength': 35, 'producer': 'Jack Daniels'},
    ]

    for item_data in whiskey_items:
        description = get_description_from_file(item_data['description_file'], 'description_whiskey.txt')
        item = Item(
            name=item_data['name'],
            price=item_data['price'],
            description=description,
            image_url=item_data['image_url'],
            isActive=item_data['isActive'],
            quantity=item_data['quantity'],
            geography=item_data['geography'],
            strength=item_data['strength'],
            producer=item_data['producer'],
            category=whiskey_category
        )
        db.session.add(item)

    cognac_category = Category.query.filter_by(name='Коньяк').first()
    if not cognac_category:
        cognac_category = Category(name='Коньяк')
        db.session.add(cognac_category)
        db.session.commit()

    cognac_items = [
        {'name': 'Tesseron Lot 90 XO Selection (в коробці)', 'price': 5768, 'description_file': 'cognac_1',
         'image_url': 'static/picture/alcohol/cognac/tesseron.png', 'isActive': True,
         'quantity': 10, 'geography': 'Франція', 'strength': 40, 'producer': 'Tesseron'},
        {'name': 'Ferrand Pineau des Charentes Blanc', 'price': 1119, 'description_file': 'cognac_2',
         'image_url': 'static/picture/alcohol/cognac/ferrand.png', 'isActive': True,
         'quantity': 10, 'geography': 'Франція', 'strength': 17, 'producer': 'Pierre Ferrand'},
        {'name': 'Ferrand Claude Chatelier VSOP (в коробці)', 'price': 2357, 'description_file': 'cognac_3',
         'image_url': 'static/picture/alcohol/cognac/claude.png', 'isActive': True,
         'quantity': 10, 'geography': 'Франція', 'strength': 40, 'producer': 'Claude Chatelier'},
        {'name': 'Godet Fins Bois 1975 (в коробці)', 'price': 28400, 'description_file': 'cognac_4',
         'image_url': 'static/picture/alcohol/cognac/godet.png', 'isActive': True,
         'quantity': 10, 'geography': 'Франція', 'strength': 40, 'producer': 'Godet'},
        {'name': 'Marquis de La Fayette, Extra Carafe', 'price': 8975, 'description_file': 'cognac_5',
         'image_url': 'static/picture/alcohol/cognac/marquis.png', 'isActive': True,
         'quantity': 10, 'geography': 'Франція', 'strength': 40, 'producer': 'Henri Mounier'},
        {'name': 'Henri Mounier, Extra Carafe', 'price': 5699, 'description_file': 'cognac_6',
         'image_url': 'static/picture/alcohol/cognac/henri.png', 'isActive': True,
         'quantity': 10, 'geography': 'Франція', 'strength': 40, 'producer': 'Maxime Trijol'},
        {'name': 'Martell VSOP', 'price': 1170, 'description_file': 'cognac_7',
         'image_url': 'static/picture/alcohol/cognac/martell.png', 'isActive': True,
         'quantity': 10, 'geography': 'Франція', 'strength': 40, 'producer': 'Martell'},
    ]
    for item_data in cognac_items:
        description = get_description_from_file(item_data['description_file'], 'description_cognac.txt')
        item = Item(
            name=item_data['name'],
            price=item_data['price'],
            description=description,
            image_url=item_data['image_url'],
            isActive=item_data['isActive'],
            quantity=item_data['quantity'],
            geography=item_data['geography'],
            strength=item_data['strength'],
            producer=item_data['producer'],
            category=cognac_category
        )
        db.session.add(item)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        add_categories_and_items()
