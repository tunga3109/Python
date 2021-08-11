import json

filename = 'json/users/username.json'

with open(filename) as f:
    user = json.load(f)
    print(f"Welcome back, {user}!")

