import os
os.device_encoding(1251)

print("Вас приветствует магазин спорт-товаров")
GOODS = ["Мячик", "Кроссовки", "Сетка"]
KINDS = ["Обычный", "Спортивный", "Профессиональный"]
COST = [9.99, 50, 20]
MULTIPLIERS = [1, 1.5, 2]
while True:
    want = input("Что бы вы хотели? (0 - для выхода)\n"+str(GOODS)+"\nВаш выбор: ")
    if want in GOODS:
        while True:
            kind = input("Какого вида вам нужен " + want + ":\n" + str(KINDS) + "\nВаш выбор: ")
            if kind in KINDS:
                count = input("Сколько " + want + " вам надо? ")
                count = int(count)
                pay = COST[KINDS.index(kind)] * count * MULTIPLIERS[KINDS.index(kind)]
                while True:
                    answer = input("Это вам выйдет в: " + str(pay) + "$\nБудете брать? [Y/N] ")
                    if answer == "Y" or answer == "y":
                        print("ЧЕК:\nКуплено: " + want + "\nВ количестве: " + str(count) + "\nСтоимость: " + str(
                            pay) + "\nСкидка на следующую покупку 30% при предъявлении этого чека")  # ctrl+alt+l
                        os.system("pause")
                        break
                    elif answer == "N" or answer == "n":
                        print("Очень жаль!! У нас есть ещё очень много других товаров, может они вам зайдут")
                        break
                    else:
                        print("Нет такого варианта ответа! только y (yes) и n (no)")
                break
            else:
                print("Нет такого варианта ответа, впишите что-нибудь из списка")
        print("Хотите купить что-нибудь ещё?")
    elif want == "0":
        print("Хорошо, будем ждать вас в следующий раз. Хорошего дня!")
        break
    else:
        print("Такого товара нет, выберите из списка")
