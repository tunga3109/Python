import telebot
from telebot import types

bot = telebot.TeleBot('1873203566:AAHp94kzfCvhzKR6w9DcYUkVi_jVfTNuCHM')

#выбор напитков
@bot.message_handler(commands=['start'])
def send_message(message):
        bot.send_message(message.from_user.id, 'Добро пожаловать, {0.first_name}\nЯ {1.first_name} 😊☕️'.format(message.from_user, bot.get_me()),parse_mode='html')
        
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        coffee = types.KeyboardButton('Кофе ☕️')
        ice_coffee = types.KeyboardButton('Айс-Кофе ❄️')
        tea = types.KeyboardButton('Чай 🍵')
        fresh = types.KeyboardButton('Фреш ❄️')
        keyboard.add(coffee,ice_coffee,tea,fresh)

        bot.send_message(message.from_user.id,text='Выберите раздел напитков: ',reply_markup=keyboard)


#Кофе
@bot.message_handler(content_types=['text'])
def send_message_coffee(message):
    if message.text == 'Кофе ☕️':
        keyboard = types.InlineKeyboardMarkup()
        latte = types.InlineKeyboardButton(text='Латте ☕️',callback_data='latte_1')
        capuccino = types.InlineKeyboardButton(text='Капучино ☕️',callback_data='capuccino_1')
        raph = types.InlineKeyboardButton(text='Раф ☕️',callback_data='raph_1')
        americano = types.InlineKeyboardButton(text='Американо ☕️',callback_data='americano_1')
        espresso = types.InlineKeyboardButton(text='Эспрессо ☕️',callback_data='espresso_1')
        flat_white = types.InlineKeyboardButton(text='Флэт-уайт ☕️',callback_data='flat_white_1')
        keyboard.add(flat_white,latte,capuccino,raph,americano,espresso)
        

        bot.send_message(message.from_user.id,text='Выберите кофе: ',reply_markup=keyboard)
    
    elif message.text == 'Айс-Кофе ❄️':
        keyboard = types.InlineKeyboardMarkup()
        ice_latte = types.InlineKeyboardButton(text='Айс-латте ☕️',callback_data='ice_latte_1')
        ice_capuccino = types.InlineKeyboardButton(text='Айс-капучино ☕️',callback_data='ice_capuccino_1')
        ice_raph = types.InlineKeyboardButton(text='Айс-раф ☕️',callback_data='ice_raph_1')
        ice_americano = types.InlineKeyboardButton(text='Айс-американо  ☕️',callback_data='ice_americano_1')
        keyboard.add(ice_americano,ice_capuccino,ice_latte,ice_raph)
        
        

        bot.send_message(message.from_user.id,text='Выберите кофе: ',reply_markup=keyboard)

    elif message.text == 'Чай 🍵':
        keyboard = types.InlineKeyboardMarkup()
        green_tea = types.InlineKeyboardButton(text='Зеленый чай', callback_data='greentea')
        black_tea = types.InlineKeyboardButton(text='Черный чай', callback_data='blacktea')
        keyboard.add(green_tea,black_tea)

        bot.send_message(message.from_user.id,text='Выберите чай',reply_markup=keyboard )
        
    elif message.text == 'Фреш ❄️':
        keyboard = types.InlineKeyboardMarkup()
        

        bot.send_message(message.from_user.id,text='Выберите кофе: ',reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id,'Я вас не понимаю\n Нажмите /start 😭😭😭')

#drinks descriptions
@bot.callback_query_handler(func= lambda call: True)
def callback_worker(call):
#coffee
    if call.data == 'latte_1':
        latte = 'Латте - кофейный напиток, который представляет собой смесь кофе и молока с пенкой.Мы готовим для вас латте маккиато (latte macchiato), вливая кофе в молоко, в результате чего на белоснежной пенке образуется кофейное пятнышко. От ближайшего родственника – капучино, наш латте отличается пропорциями ингредиентов: значительно большим количеством молока и относительно низкой молочной пенкой.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_latte = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_latte)
        bot.send_message(call.from_user.id, latte,reply_markup=key) 
    elif call.data == 'capuccino_1':
        capuccino = 'Капучино – это не просто кофе с молоком, а настоящее наслаждение под пышной шапкой из молочной пенки.Наш капучино гармонично сочетает в себе натуральную сливочную сладость молока и яркий сбалансированный эспрессо.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_capuccino = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_capuccino)
        bot.send_message(call.from_user.id, capuccino,reply_markup=key) 
    elif call.data == 'raph_1':
        raph = 'Раф кофе - это сочетание эспрессо, ванильного сахара и жидких сливок, которые взбиваются вместе, образуя нежную и лёгкую консистенцию.Раф кофе от Hotfix имеет свою характерную изюминку - лёгкие пряные сливочные нотки в послевкусии и воздушная консистенция, которая как сахарная вата тает во рту.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_raph = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_raph)
        bot.send_message(call.from_user.id, raph, reply_markup=key) 
    elif call.data == 'americano_1':
        americano = 'Кофе Американо состоит из двойного зспрессо и горячей воды.В рецепте приготовления наш американо отличается крепостью и способом приготовления. Сначала наливается горячая вода, а затем – двойной эспрессо. Так крема не трескается, а остаётся плотной и равномерной, концентрируя ароматические вещества.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_raph = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_raph)
        bot.send_message(call.from_user.id, americano, reply_markup=key)
    elif call.data == 'espresso_1':
        espresso = 'Эспрессо (итал. Espresso) – это баланс запаха и вкуса: сладости, горчинки и лёгкой кислинки. Оттенки вкуса зависят от сортов кофейных зёрен, входящих в состав смеси, и степени обжарки.Наш эспрессо с богатым насыщенным шоколадным вкусом и карамельными сладкими нотами – сердце всех кофейных напитков Hotfix.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_espresso = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_espresso)
        bot.send_message(call.from_user.id, espresso, reply_markup=key) 
    elif call.data == 'flat_white_1':
        flat_white = 'Флет Уайт – это такое сочетание двойного эспрессо и молока, где ни один ингредиент не перебивает вкус другого.Наш флет уайт - это идеальная грань между эспрессо и капучино с тонкой сливочной молочной пенкой, образующей ровную глянцевую поверхность.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_flat_white = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_flat_white)
        bot.send_message(call.from_user.id, flat_white, reply_markup=key) 


#ice coffee
    if call.data == 'ice_latte_1':
        ice_latte = 'Латте - кофейный напиток, который представляет собой смесь кофе и молока с пенкой.Мы готовим для вас латте маккиато (latte macchiato), вливая кофе в молоко, в результате чего на белоснежной пенке образуется кофейное пятнышко. От ближайшего родственника – капучино, наш латте отличается пропорциями ингредиентов: значительно большим количеством молока и относительно низкой молочной пенкой.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_ice_latte = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_ice_latte)
        bot.send_message(call.from_user.id, ice_latte, reply_markup=key)
    elif call.data == 'ice_capuccino_1':
        ice_capuccino = 'Айс-капучино - нежная кофейная пенка, которая представляет собой взбитый эспрессо на молоке со льдом.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_ice_cappuccino = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_ice_cappuccino)
        bot.send_message(call.from_user.id, ice_capuccino, reply_markup=key) 
    elif call.data == 'ice_raph_1':
        ice_raph = 'Если вы привязались к рафу, в этом нет ничего удивительного. Его воздушная кофейно-сливочная текстура так и заманивает взять очередной стаканчик… К счастью, смесь взбитого эспрессо со сливками и ванильным сахаром есть и в холодном варианте.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_ice_raph = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_ice_raph)
        bot.send_message(call.from_user.id, ice_raph, reply_markup=key)  
    elif call.data == 'ice_americano_1':
        ice_americano = 'Айс-американо прекрасно утоляет жажду в жаркий день и придает энергии.В нем нет ничего лишнего, только эспрессо со льдом, в который вам могут добавить сливки или сироп.'
        key = types.InlineKeyboardMarkup(row_width=3)
        order_ice_americano = types.InlineKeyboardButton(text='Попробовать😋',url='https://hotfixcafe.by/coffee-shops/')
        key.add(order_ice_americano)
        bot.send_message(call.from_user.id, ice_americano, reply_markup=key)   

# 
  
    

bot.polling(none_stop=True, interval=0)



    

