from app import db, Category, Item, app
from get_description import get_description_from_file

def add_categories_and_items():
    whiskey_category = Category.query.filter_by(name='Віскі').first()
    if not whiskey_category:
        whiskey_category = Category(name='Віскі')
        db.session.add(whiskey_category)
        db.session.commit()


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

    beer_category = Category.query.filter_by(name='Пиво').first()
    if not beer_category:
        beer_category = Category(name='Пиво')
        db.session.add(beer_category)
        db.session.commit()

    beer_items = [
        {'name': 'Пиво «Оболонь» світле с/п', 'price': 32.90, 'description_file': 'beer_1',
         'image_url': 'static/picture/alcohol/beer/Obolon.png', 'isActive': True,
         'quantity': 10, 'geography': 'Україна', 'strength': 4.5, 'producer': 'AB InBev'},
        {'name': 'Stella Artois', 'price': 26.90, 'description_file': 'beer_2',
         'image_url': 'static/picture/alcohol/beer/stella.png', 'isActive': True,
         'quantity': 10, 'geography': 'Україна', 'strength': 5, 'producer': 'AB InBev'},
        {'name': 'Пиво Senor Cartel світле', 'price': 42.50, 'description_file': 'beer_3',
         'image_url': 'static/picture/alcohol/beer/cartel.png', 'isActive': True,
         'quantity': 10, 'geography': 'Україна', 'strength': 4.5, 'producer': 'Senor Cartel'},
        {'name': 'Kurpfalz Brau Helles світле', 'price': 83, 'description_file': 'beer_4',
         'image_url': 'static/picture/alcohol/beer/helles.png', 'isActive': True,
         'quantity': 10, 'geography': 'Німеччина', 'strength': 5.2, 'producer': 'Kurpfalz Brau'},
        {'name': 'Пиво Peroni', 'price': 120, 'description_file': 'beer_5',
         'image_url': 'static/picture/alcohol/beer/peroni.png', 'isActive': True,
         'quantity': 10, 'geography': 'Італія', 'strength': 4.7, 'producer': 'Peroni Brewery'},
        {'name': 'Corona Extra', 'price': 669, 'description_file': 'beer_6',
         'image_url': 'static/picture/alcohol/beer/corona.jpg', 'isActive': True,
         'quantity': 10, 'geography': 'Мексика', 'strength': 4.5, 'producer': 'Corona'},
        {'name': 'Закарпатське Оригінальне світле', 'price': 29, 'description_file': 'beer_7',
         'image_url': 'static/picture/alcohol/beer/Zakarpatske.png', 'isActive': True,
         'quantity': 10, 'geography': 'Україна', 'strength': 4, 'producer': 'ПАТ Оболонь'},
        {'name': 'Львівське світле фільтроване', 'price': 33, 'description_file': 'beer_8',
         'image_url': 'static/picture/alcohol/beer/lvivske_light.png', 'isActive': True,
         'quantity': 10, 'geography': 'Україна', 'strength': 4.5, 'producer': 'Львівська пивоварня'},
        {'name': 'Львівське Лев темне', 'price': 36, 'description_file': 'beer_9',
         'image_url': 'static/picture/alcohol/beer/lvivske.jpg', 'isActive': True,
         'quantity': 10, 'geography': 'Україна', 'strength': 4.7, 'producer': 'Львівська пивоварня'},
        {'name': 'Чернігівське, світле, фільтроване', 'price': 39, 'description_file': 'beer_10',
         'image_url': 'static/picture/alcohol/beer/Chernigyvske.jpg', 'isActive': True,
         'quantity': 10, 'geography': 'Україна', 'strength': 4.6, 'producer': 'Чернігівська броварня'},
        {'name': 'Warsteiner Brauerei світле', 'price': 60, 'description_file': 'beer_11',
         'image_url': 'static/picture/alcohol/beer/wastiner.png', 'isActive': True,
         'quantity': 10, 'geography': 'Німеччина', 'strength': 5.3, 'producer': 'Krombacher Brauerei'},
        {'name': 'Original Guinness темне фільтроване', 'price': 90, 'description_file': 'beer_12',
         'image_url': 'static/picture/alcohol/beer/guinness.png', 'isActive': True,
         'quantity': 10, 'geography': 'Ірландія', 'strength': 4.8, 'producer': 'Guinness & Co'},
    ]

    for item_data in beer_items:
        description = get_description_from_file(item_data['description_file'], 'description_beer.txt')
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
            category=beer_category
        )
        db.session.add(item)

    gin_category = Category.query.filter_by(name='Джин').first()
    if not gin_category:
        gin_category = Category(name='Джин')
        db.session.add(gin_category)
        db.session.commit()

    gin_items = [
        {'name': 'Stirling Pink Gin', 'price': 459, 'description_file': 'gin_1',
         'image_url': 'static/picture/alcohol/gin/stirlingpink.png', 'isActive': True,
         'quantity': 10, 'geography': 'Нідерланди', 'strength': 37.5, 'producer': 'Stirling'},
        {'name': 'LoneWolf Gin', 'price': 1290, 'description_file': 'gin_2',
         'image_url': 'static/picture/alcohol/gin/lonewolf.png', 'isActive': True,
         'quantity': 10, 'geography': 'Шотландія', 'strength': 40, 'producer': 'BrewDog'},
        {'name': 'Chocolate Orange Gin', 'price': 1190, 'description_file': 'gin_3',
         'image_url': 'static/picture/alcohol/gin/chocolateorange.png', 'isActive': True,
         'quantity': 10, 'geography': 'Великобританія', 'strength': 46, 'producer': 'TBGC'},
        {'name': 'Bombay Sapphire', 'price': 1190, 'description_file': 'gin_4',
         'image_url': 'static/picture/alcohol/gin/bombay.png', 'isActive': True,
         'quantity': 10, 'geography': 'Великобританія', 'strength': 47, 'producer': 'Bombay'},
        {'name': 'Daucourt New Angouleme', 'price': 1190, 'description_file': 'gin_5',
         'image_url': 'static/picture/alcohol/gin/daucourt.png', 'isActive': True,
         'quantity': 10, 'geography': 'Франція', 'strength': 43, 'producer': 'Daucourt Martin Distillery'},
    ]

    for item_data in gin_items:
        description = get_description_from_file(item_data['description_file'], 'description_gin.txt')
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
            category=gin_category
        )
        db.session.add(item)

    wine_category = Category.query.filter_by(name='Вино').first()
    if not wine_category:
        wine_category = Category(name='Вино')
        db.session.add(wine_category)
        db.session.commit()

    wine_items = [
        {'name': 'Вино сухе біле Teruzzi Terre Di Tufi IGT', 'price': 1054, 'description_file': 'wine_1',
         'image_url': 'static/picture/alcohol/wine/terre.png', 'isActive': True,
         'quantity': 10, 'geography': 'Італія', 'strength': 12.5, 'producer': 'Teruzzi'},
        {'name': 'Вино Glou Glou, Orange, Fio Wine, бурштинове сухе', 'price': 775, 'description_file': 'wine_2',
         'image_url': 'static/picture/alcohol/wine/glou.png', 'isActive': True,
         'quantity': 10, 'geography': 'Німеччина', 'strength': 12.5, 'producer': 'Teruzzi'},
        {'name': 'Вино сухе червоне Col d’Orcia Poggio al Vento Brunello di Montalcino Riserva 2012', 'price': 6999, 'description_file': 'wine_3',
         'image_url': 'static/picture/alcohol/wine/col.png', 'isActive': True,
         'quantity': 10, 'geography': 'Італія', 'strength': 14.5, 'producer': 'Col dOrcia'},
        {'name': 'Вино сухе червоне Teruzzi Melograni Toscana Rosso IGT', 'price': 1450, 'description_file': 'wine_4',
         'image_url': 'static/picture/alcohol/wine/melograni.png', 'isActive': True,
         'quantity': 10, 'geography': 'Італія', 'strength': 12.5, 'producer': 'Teruzzi'},
        {'name': 'Вино Vilarissa Valley, Douro Tinto, Barao de Vilar, червоне напівсухе', 'price': 375, 'description_file': 'wine_5',
         'image_url': 'static/picture/alcohol/wine/valley.png', 'isActive': True,
         'quantity': 10, 'geography': 'Португалія', 'strength': 12.5, 'producer': 'Barao de Vilar'},
        {'name': 'Вино El Emperador, Merlot, червоне сухе', 'price': 279, 'description_file': 'wine_6',
         'image_url': 'static/picture/alcohol/wine/el.png', 'isActive': True,
         'quantity': 10, 'geography': 'Чилі', 'strength': 12.5, 'producer': 'Vina del Nuevo Mundo'},
    ]

    for item_data in wine_items:
        description = get_description_from_file(item_data['description_file'], 'description_wine.txt')
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
            category=wine_category
        )
        db.session.add(item)



    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        add_categories_and_items()
