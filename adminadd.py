from app import db, User, app

def add_admin():
    """Додає адмінів у базу даних."""
    users = [
        {'username': 'aeustosibrevia', 'password': 'adminpass1', 'email': 'aeustosibrevia@example.com', 'isAdmin': True,
         'phone_number': '+380631970036', 'first_name': 'Андрій', 'second_name': 'Соха'},
        {'username': 'mrpuzirik', 'password': 'adminpass2', 'email': 'user1@example.com', 'isAdmin': True,
         'phone_number': '+380631110055', 'first_name': 'Андрій', 'second_name': 'Шевчук'},
        {'username': 'yalovitsaa', 'password': 'adminpass2', 'email': 'user2@example.com', 'isAdmin': True,
         'phone_number': '+380630005511', 'first_name': 'Анастасія', 'second_name': 'Яловіца'},
    ]

    for user_data in users:
        new_user = User(
            username=user_data['username'],
            email=user_data['email'],
            isAdmin=user_data['isAdmin'],
            phone_number=user_data['phone_number'],
            first_name=user_data['first_name'],
            second_name=user_data['second_name']
        )
        new_user.set_password(user_data['password'])
        db.session.add(new_user)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        add_admin()