#номер 1

#a = [1,2,2,3,4,3,7,4,5,9,6,7,8]
#print(set(a))

#номер 2

#a = [1,2,2,3,3,4,5,5,6,6,7,5,4]
#b = [5,6,4,43,5,3,3,2,2,1,2,3,4,6,6,6]
#c = set(a).intersection(set(b))
#
#print(f'{len(c)} пар')



#номер 3

#C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
#C_2 = (45, 21,124,76,5,23,91,234)
#
#if sum(C_2) > sum(C_1):
#    print(f'Сумма больше в кортеже - {sum(C_2)}')
#else:
#    print(f'Сумма больше в кортеже - {sum(C_1)}')
#
#print(f'Индэксы минимальных и максимальных элементов 1-го кортежа:{C_1.index(max(C_1))} и {C_1.index(min(C_1))}')
#print(f'Индэксы минимальных и максимальных элементов 2-го кортежа:{C_2.index(max(C_2))} и {C_2.index(min(C_2))}')

#номера 4

#quote = ' An apple a day keeps keeps the doctor away'.replace(' ','').lower()
#d = {}
#for letter in quote:
#    d.setdefault(letter,0)
#    if letter in d:
#        d[letter] += 1
#print(d)

#номер 5

#good = input('Какой товар: ')
#count = int(input('Кол-во: '))
#sweet_house = {'Круассан':[('Мука','Соль','Сахар','Круассан'),5,count]}
#sweet_house['Круассан'][2] = count
#sostav = sweet_house['Круассан'][0]
#price = sweet_house['Круассан'][1]
#while True:
#    if good == 'Круассан':
#        choice = int(input('\nсостав - 1\nцена - 2\nкол-во - 3\nПокупка - 4\nВыход - 0\n'))
#        if choice == 1:
#            print(f'Состав: {list(sostav)}')
#        elif choice == 2:
#            print(f'Цена: {price} рублей за 100 грамм')
#        elif choice == 3:
#            print(f'Кол-во: {count}')
#        elif choice == 4:
#            buy = input('Что хотите купить? ')
#            skolko = int(input('Сколько: '))
#            if buy == 'Круассан':
#                buy_1 = count * price
#                if count > skolko:
#                    count -= skolko
#        elif choice == 0:
#            print(f'вы купили {buy} на сумму {buy_1}\nОсталось {count} штук')
#            break

#номер 6

#a = [1,2,3,4,5,6,7]
#b = [3,2,1]
#c = set(a).intersection(set(b))
#print(f'{len(c)} числа содержаться одновременно и в первом, и во втором: {c}')



#Номер 7

#try :
#    a = int(input('Первое число: '))
#    b = int(input('Второе число: '))
#    c = a/b
#except ZeroDivisionError:
#    print('На ноль делить нельзя !!')
#else:
#    print(c)
#finally:
#    print('Программа пристановлена')

#номер 8

#filename = ''
#
#with open(filename,'a',encoding='utf-8') as f:
#    d = {}
#    for i in range(3):
#        student = input('Имя студента:')
#        marks = int(input('Оценка: '))
#        d[student] = marks
#        f.write(f'{student} : {marks}\n')
#    stud_1 = []
#    count = 0
#    wunderkind = []
#    for stud, mark in d.items():
#        stud_1.append(stud)
#        if mark > 3:
#            wunderkind.append(stud)
#        count += mark
#
#    print(f'Студенты - отличники: {wunderkind}')
#    print(f'Средний балл: {count/len(stud_1)}')
