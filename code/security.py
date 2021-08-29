from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'Andrés', 'hola1234'),
    User(33, 'jose', 'gato77')
]

username_mapping = {u.username: u for u in users}  # Create: {'Andrés': {1, 'Andrés', 'hola1234'}}
userid_mapping = {u.id: u for u in users}  # Create: {1: {1, 'Andrés', 'hola1234'}}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)


