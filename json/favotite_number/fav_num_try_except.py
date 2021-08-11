import json

filename = 'json/favotite_number/fav_num.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    fav_num = int(input('Enter your num: '))
    with open(filename,'w') as f:
        json.dump(fav_num,f)
else:
    print(f'Я знаю ваше любимое число! Это {number}')