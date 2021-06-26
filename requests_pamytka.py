import requests

#Получение разметки
result = requests.get('https://letpy.com/simple-html-example/')
print(result.text)

#1 рандомное число
import requests

result = requests.get('https://letpy.com/simple-html-example/')
result_text = result.text
a = []
for num in result_text[318::]:
    if num.isdigit():
        a.append(num)

num_split = ''.join(a)
print(num_split)

# через requests и Json
import requests
import json

result = requests.get('https://www.nbrb.by/api/exrates/rates/usd?parammode=2')
data = json.loads(result.text)
print(data["Cur_OfficialRate"])


#Получение сообщения
import requests

last_update_id = 0
while True:
    result = requests.get(
        'Тут должен быть адрес для вашего бота',
        params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:
        print(update['message']['text'])
        last_update_id = update['update_id']


#Получение одного и того же сообщения от бота
import requests

last_update_id = 0

while True:
    result = requests.get(
        'https://api.telegram.org/bot1763770488:AAHH9kdrIhuDwzAnw6Mc6n67FN7LlDdDICk/getUpdates',
        params={'offset': last_update_id + 1}) # 0 + 1 сообщение
    data = result.json() # json формат
    for update in data['result']:
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']

        send_result = requests.get(
            'https://api.telegram.org/bot1763770488:AAHH9kdrIhuDwzAnw6Mc6n67FN7LlDdDICk/sendMessage',
            params={'chat_id': chat_id, 'text': 'Привет от LETPY'}
            )


{'ok': True, 

    'result':[
        {'update_id': 399761507,
            'message': 
                {'message_id': 2, 
                    'from':
                            {'id': 125454804, 'is_bot': False, 
                                'first_name': 'Sergey',
                                 'last_name': 'Kotov',
                                  'username': 'kotov_dev',
                                  'language_code': 'en'},





    'chat':
            {
            'id': 125454804,
             'first_name': 'Sergey', 
             'last_name': 'Kotov',
             'username': 'kotov_dev', 
             'type': 'private'},
            'date': 1603456852, 
            'text': 'Привет, мой первый бот!'
                                                }
                                            }
                                        ]
                                    }