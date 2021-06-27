import telebot
import config

bot = telebot.TeleBot(config.token)

from telebot import types

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, '🎸🎸🎸 Добро пожаловать, {0.first_name}!!!\n Мы магазин музыкальных инструментов 🎸🎸🎸')
        
        keyboard = types.InlineKeyboardMarkup()

        guitars = types.InlineKeyboardButton(text='Гитары 🎸',callback_data='guitars')
        keyboard.add(guitars)
        ukulele = types.InlineKeyboardButton(text='Укулеле 🎸',callback_data='ukulele')
        keyboard.add(ukulele)
        bass_guitar = types.InlineKeyboardButton(text='Басс-гитары 🎸',callback_data='bass_guitars')
        keyboard.add(bass_guitar)

        bot.send_message(message.from_user.id,text='🎸 Выберите музыкальный инструмент: 🎸', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'guitars':
        keyboard = types.InlineKeyboardMarkup(row_width=3)

        guitars_1 = types.InlineKeyboardButton(text='Классическая 🎸',callback_data='сlassic',url='https://muzshop.by/catalog/category/gitary_klassicheskie')
        keyboard.add(guitars_1)
        guitars_2 = types.InlineKeyboardButton(text='Акустическая 🎸',callback_data='acoustic',url='https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjzitK7gevwAhXxCwYAHUSgDm8YABABGgJ3cw&ae=2&ohost=www.google.com&cid=CAESQeD2ca4YwxyUSHySm2akzrRydNYwr8HVI8kdAciSYAbdMFMQb9Ez7aVGyh4TtFm_Fnopvc4Ulzjpr561vMVwaZ81&sig=AOD64_1FSTZwzUlKOAF8ERMRyTYc_hUv0Q&q&adurl&ved=2ahUKEwi2hsu7gevwAhUSlhQKHYVsB6EQ0Qx6BAgDEAE&dct=1')
        keyboard.add(guitars_2)

        bot.send_message(call.from_user.id, text='Выбери тип гитары: ', reply_markup=keyboard)

    elif call.data == 'ukulele':
        keyboard = types.InlineKeyboardMarkup(row_width=3)

        ukulele_1 = types.InlineKeyboardButton(text='4-струнные 🎸',callback_data='string_4')
        keyboard.add(ukulele_1)
        ukulele_2 = types.InlineKeyboardButton(text='3-хструнные 🎸',callback_data='string_3')
        keyboard.add(ukulele_2)



        bot.send_message(call.from_user.id, text='🎸 Выбери тип укулеле: 🎸 ', reply_markup=keyboard)


    
    

bot.polling(none_stop=True)

