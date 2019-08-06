def add_user(name, secret_word):
    user_object = User(username=name,  password=secret_word)
    session.add(user_object)
    session.commit()


def get_user(name):
    return session.query(User).filter(username=name).first()