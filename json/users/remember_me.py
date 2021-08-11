import json

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'json/users/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя."""
    
    username = input("What is your name? ")
    filename = 'json/users/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():

    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'json/users/username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")

greet_user()
get_new_username()

