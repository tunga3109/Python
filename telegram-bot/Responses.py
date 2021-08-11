from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower() #ввод текста от пользователя

    if user_message in ('привет', 'hi', 'sup'): # если будут эти слова...
        return "Hey! How's it going?" #... бот выдаст это сообщение
    
    if user_message in ('who are you', 'who are you?'):
        return "I am Bel Bot!"
    
    if user_message in ('пошел нахуй', 'who are you?'):
        return "Сам пошел нахуй,больной ублюдок!"
    
    if user_message in ('нет,ты пошел нахуй'):
        return "Нет,ты пошел нахуй!"
    
    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime(' %d/%m/%y, %H:%M:%S')

        return str(date_time)

    return "I don't understand you!" #если будет что-то непонятно....





