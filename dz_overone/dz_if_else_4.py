shop = int(input('Выберите товар:\nКупить - 1\n расчитать - 2\nвыход - 3\n'))
count_con = 0
if shop == 1:
    choice = int(input('Выберите товар:\nпиво - 1\nрыбка - 2\nшампанское - 3\n'))
    if choice == 1:
        price = 300
        count = int(input('kol-vo: '))
        price *= count
        price += count_con
        print(price)
    elif choice == 2:
        price = 200 
        count = int(input('kol-vo: '))
        price *= count
        price += count_con
        print(price)
    elif choice == 3:
        price = 2000
        count = int(input('kol-vo: '))
        price *= count
        price += count_con
        print(price)

        
    

    




