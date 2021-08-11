#Чтение файла json
import json 

filename = 'json/part_1/numbers.json'
with open(filename) as f:
    num = json.load(f)

print(num)