#Ввод данных и сохранение в файле json
import json

username = input('Enter your name: ')

filename = 'json/users/username.json'
with open(filename,'w') as f:
    json.dump(username,f)
    print(f"We'll remember you when you come back, {username}!")