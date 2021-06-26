import telebot

bot = telebot.TeleBot('1797546809:AAH37-9uxfRD-S03nCNh2uAWl7KwuCRsdPs')

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('/Users/tunga3109/Desktop/PYTHON/tgbot/sticker/sticker.webp', 'rb') #импортируем стикер тг
    bot.send_sticker(message.from_user.id, sti)

    bot.send_message(message.from_user.id, 'Привет,{0.first_name},меня зовут {1.first_name}'.format(message.from_user, bot.get_me()),parse_mode='html') 

@bot.message_handler(content_types=['text'])
def send_message(message):
    bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True)