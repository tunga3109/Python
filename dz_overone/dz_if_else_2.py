#Wikipedia 
while True:
    print('Python - 1\nС++ - 2\nJava - 3\nKotlin - 4')

    choose_lang_of_prog = int(input('Выберите язык программирования(1 - 4): '))
    if choose_lang_of_prog == 1:
        print('Python - 20 февраля 1991, Гвидо ван Россум')
        know_about_it = input('Вы знали об этом? ')
        if know_about_it =='да':
            print('OK')
        elif know_about_it == 'нет':
            check_the_knowledges = int(input('Когда этот язык создан? '))
            if check_the_knowledges == 1991:
                print('Правильно!')
            else:
                print('Неправильно!')
    elif choose_lang_of_prog == 2:
        print('C++ - 1983, Бьёрн Страуструп')
        know_about_it = input('Вы знали об этом? ')
        if know_about_it =='да':
            print('OK')
        elif know_about_it == 'нет':
            check_the_knowledges = int(input('Когда этот язык создан? '))
            if check_the_knowledges == 1983:
                print('Правильно!')
            else:
                print('Неправильно!')
    elif choose_lang_of_prog == 3:
        print('Java - 1995, Джеймс Гослинг')
        know_about_it = input('Вы знали об этом? ')
        if know_about_it =='да':
            print('OK')
        elif know_about_it == 'нет':
            check_the_knowledges = int(input('Когда этот язык создан? '))
            if check_the_knowledges == 1995:
                print('Правильно!')
            else:
                print('Неправильно!')
    elif choose_lang_of_prog == 4:
        print('Kotlin - 22 июля 2011, JetBrains')
        know_about_it = input('Вы знали об этом? ')
        if know_about_it =='да':
            print('OK')
        elif know_about_it == 'нет':
            check_the_knowledges = int(input('Когда этот язык создан? '))
            if check_the_knowledges == 2011:
                print('Правильно!')
            else:
                print('Неправильно!')
    else:
        print('Введите число!')