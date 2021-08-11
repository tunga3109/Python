import time
while True:
    choice = int(input('Выберите меню:\nБот - 1\nСделать заказ - 2\nВыйти - 3'))
    if choice == 1:
        print('Здраствуйте,я Бот')
        kolvo = int(input('Скажите сколько картин вы хотили бы преобрести? '))
        budget = int(input('Скажите какой у вас бюджет? '))
        budget /= kolvo
        time.sleep(4)
        print(budget)
    elif choice == 2:
        pass
    elif choice == 3:
        print('goodbye')