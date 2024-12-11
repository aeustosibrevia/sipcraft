from app import db, User, app

def add_admin():
    """Додає адмінів у базу даних."""
    users = [
        {'username': 'aeustosibrevia', 'password': 'adminpass1', 'email': 'aeustosibrevia@example.com', 'isAdmin': True},
        {'username': 'mrpuzirik', 'password': 'adminpass2', 'email': 'user1@example.com', 'isAdmin': True},
        {'username': 'yalovitsaa', 'password': 'adminpass2', 'email': 'user2@example.com', 'isAdmin': True},
    ]

    for user_data in users:
        new_user = User(
            username=user_data['username'],
            email=user_data['email'],
            isAdmin=user_data['isAdmin']
        )
        new_user.set_password(user_data['password'])
        db.session.add(new_user)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        add_admin()