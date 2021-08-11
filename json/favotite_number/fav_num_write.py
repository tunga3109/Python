import json

fav_num = int(input('Your favotite number: '))

filename = 'json/favotite_number/fav_num.json'

with open(filename, 'w') as f:
    json.dump(fav_num,f)

