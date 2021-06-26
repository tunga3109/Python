import requests


last_update_id = 0
while True:
    result = requests.get(
        'https://api.telegram.org/bot1763770488:AAHH9kdrIhuDwzAnw6Mc6n67FN7LlDdDICk/getUpdates',
        params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:
        print(update['message']['text'])
        last_update_id = update['update_id']









        
    








