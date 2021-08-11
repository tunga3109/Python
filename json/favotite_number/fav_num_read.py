import json

filename = 'json/favotite_number/fav_num.json'

with open(filename) as f:
    number = json.load(f)

print(f'Я знаю ваше любимое число! Это {number}')