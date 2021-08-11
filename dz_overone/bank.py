#Банк

#Регистрация
def registration():   
    print('Вас приветствует Банк!')

    name = input('Введите ваше имя:')
    print('Здраствуйте,', name)

    for i in range(3):
        phone = input('Номер телефона: ')
        if phone[0] == '+' and phone[1:4] == '375' and len(phone) == 13:
            print(phone)
            break
        else:
            print('Введи нормальный белорусский номер!!')
    else:
        print('Мы вас заблокировали, досвидания')

    for i in range(3):
        email = input('Почта: ')
        if '@' in email:
            if '.' in email[email.index('@'):]:
                print(email)
                break
        else:
            print('Ошибка')

    for i in range(3):
        card_num = input('Номер карты: ')
        if len(card_num) == 12:
            print(card_num)
            break
        
    money = int(input('Сколько денег: '))
    print(f'\tНа вашем счету: {money} рублей')

#С карты на другую карту
def send_to_card():
    while True:
            your_card = input('Введите вашу карту: ')
            if len(your_card) == 16 and your_card.isdigit():
                not_your_card = input('Введите карту клиента: ')
                if len(not_your_card) == 16 and not_your_card.isdigit():
                    data_of_your_card = input('Введите до какого числа карта: ')
                    if '/' in data_of_your_card and len(data_of_your_card) == 5:
                        summa = int(input('Какую сумму переводить: '))
                        if money > summa:
                            money -= summa
                            print(f'На вашем счету {money}')
                            break
                        else:
                            print('Недостаточно средств')
                    else:
                        print('Введите корректную дату: ')
                else:
                    print('Введите корректные данные:')
            else:
                print('Введите корректные данные:')
            break

#На номер телефона
def send_to_mobile():
    while True:
            operator = int(input('\n\tМтс - 1\n\tА1 - 2\n\tLife - 3\n\t'))
            if operator == 1:
                phone_number = input('Введите номер вашего телефона:\n')
                if phone_number[0:4] == '+375' and len(phone_number) == 13 and phone_number[4:6] == '33':
                    for i in range(3):
                        how_many = int(input('Введите сумму:'))
                        if how_much < money:
                            money -= how_much
                            print(f'\tНа вашем счету {money}')
                            break
                        else:
                            print('Недостаточно средств')
                break
            if operator == 2:
                while True:
                    phone_number = input('Введите номер вашего телефона:\n')
                    if phone_number[0:4] == '+375' and len(phone_number) == 13 and phone_number[4:6] == '44':
                        for i in range(3):
                            how_many = int(input('Введите сумму:'))
                            if how_many < money:
                                money -= how_many
                                print(f'\tНа вашем счету {money}')
                                break
                            else:
                                print('Недостаточно средств')
                    break
            if operator == 3:
                while True:
                    phone_number = input('Введите номер вашего телефона:\n')
                    if phone_number[0:4] == '+375' and len(phone_number) == 13 and phone_number[4:6] == '25':
                        for i in range(3):
                            how_many = int(input('Введите сумму:'))
                            if how_many < money:
                                money -= how_many
                                print(f'\tНа вашем счету {money}')
                                break
                            else:
                                print('Недостаточно средств')
                    else:
                        print('Введите еще раз')
                    break

#Запуск
while True:
    menu = int(input('\tВыберите меню:\n\tРегистрация - 1\n\tПеревод с одной карты на другую карту - 2\n\tМобильная связь - 3\n\tВыход - 0\n '))
    if menu == 1:
        registration()
    if menu == 2:
        send_to_card()
    if menu == 3:
        send_to_mobile()
    if menu == 0:
        break

    
print(f'\tНа вашем счету {money}')