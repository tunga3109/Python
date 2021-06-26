#print(abs(-4)) #возвращает положительное число
#divmod(a,-11) #принимающая число и делитель. Она возвращает пару чисел:
# результат целочисленного деления и остаток от деления

#Палиндром
string = input()
string = string.lower().replace(' ', '')
a = string.lower().replace(' ','')
a = string[::-1]
if string == a:
    print('Yes')
else:
    print('No')


#Звездочки
num = input()
if len(num) >= 8 and num.isdigit():
    b = num[-4:]
    a = len(num) - 4
    print("*" * a + b)
else:
    print('Ошибка')

#самое длинное слово
string = input()
words = string.split()
longest_word = ''

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)  

#Поиск слов по кол-во
string = input('Предложение:')
word = input(' Cлово которое ищешь')
string = string.lower()
string = string.replace(",", " ")
string = string.replace(".", " ")
words = string.split()
word = word.lower()
print(words.count(word))

#Число в предложении
string = input()
words = string.split(' ')
numbers = []

for elem in words:
    if elem.isdigit():
        if elem not in numbers:
            numbers.append(int(elem))
        
    

print(sorted(numbers))


#факториял
def factorial(n):
    result = 1
    for n in range (n+1):
        result *= n + 1
    print('Факториал числа ', n, ' - ', result)
user_input = int(input('Enter a figure'))
factorial(user_input)

#шифрование Цезаря
def encrypt(a, k):
    string = "" #пустое слово
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    a = str(a).upper()
    for el in a:
        if el.isalpha() and el in letters: #если ел буква и ел в алфавите
            b = el.replace(a[a.index(el)], letters[(letters.index(el)+k) % 33]) #меняем местами 
            string += b
        else:
            b = el
            string += b
    return string
encrypted_message = encrypt("ПРИВЕТ GDR!", -1)
print(encrypted_message)

#Загаданное число
import random

number = random.randint(1, 100)
print(number)

for i in range(3):
    z = int(input())
    if number > z:
        print('Загаданное число больше')
    elif number < z:
        print('Загаданное число меньше')
    else:
        print('Вы выиграли')
        break
else:
    print('Вы проиграли')

#weather
months = {
        1: 'Январе',
        2: 'Феврале',
        3: 'Марте',
        4: 'Апреле',
        5: 'Мае',
        6: 'Июне',
        7: 'Июле',
        8: 'Августе',
        9: 'Сентябре',
        10: 'Октябре',
        11: 'Ноябре',
        12: 'Декабре'
    }

def season_events(number_of_month):
    if not isinstance(number_of_month, int) or 1 <= number_of_month <= 12:
        print('error')
        
    if number_of_month == 1 or number_of_month == 2 or number_of_month == 12:
        print(f'Вы родились в {months[number_of_month]}. За окном падал белый снег')
    elif number_of_month == 3 or number_of_month == 4 or number_of_month == 5:
        print('Птицы пели прекрасные песни')
    elif number_of_month == 6 or number_of_month == 7 or number_of_month == 8:
        print('Солнце светило ярче чем когда-либо')
    elif number_of_month == 9 or number_of_month == 10 or number_of_month == 11:
        print('Урожай был невероятным')
    else:
        print('error')
    
    

season_events('rfldkf')   

#ID
def get_drink_ID(fruit, size):
    num = []
    fru = []

    fruit_abb = fruit.upper()
    size_abb = size.upper()
    fruits = fruit_abb.split() #строку в список

    for elem in fruits:
        fru.append(elem[:3])
        fru_1 = ''.join(fru) #объединение в одно слово
        

    for elem_1 in size_abb:
        if elem_1.isdigit():
            num.append(elem_1)
            num_1 = ''.join(num)
            
    
    return  fru_1 + num_1
    
        
    
print(get_drink_ID('passion fruit','50000ml'))


#подсчет товаров
catalog = {}

for i in range(3):
    tovar = input()
    kolvo = int(input())
    if tovar in catalog:
        catalog[tovar] += kolvo
    else:
        catalog[tovar] = kolvo
        
with open('example.txt', 'r+') as f:
    for line in f:
        print(line)

#Подсчет товаров
catalog = {}

for i in range(10):
    name = input()
    count = int(input())
    if name in catalog:
        catalog[name] += count
    else:
        catalog[name] = count

with open('example.txt', 'w+') as f:
    for k,v in catalog.items():
        f.write(f'{k} : {v}')

#json
import json

catalog = {}

with open('catalog.json','r') as f:
    content = f.read()
    catalog = json.loads(content)

for i in range(3):
    name = input()
    count = int(input())
    if name in catalog:
        catalog[name] += count
    else:
        catalog[name] = count

with open('catalog.json','w') as f:
    content = json.dumps(catalog)
    f.write(content)


#CSV
import csv

catalog = {}

with open('catalog.csv', 'r') as f:
    # читаем файл csv построчно и сразу распаковываем
    # каждую строку в две переменных
    for name, count in csv.reader(f):
        catalog[name] = int(count)

for i in range(3):
    name = input('Введите наименование товара')
    count = int(input('Введите количество товара'))
    # если ключ (наименование товара) уже есть
    # в словаре
    if name in catalog:
        # увеличиваем его значение на count
        catalog[name] += count
    else:
        # иначе создаем ключ со значением count 
        catalog[name] = count

# Каждый ключ и значение в каталоге нужно 
# записать в файл. Метод словаря items
# возвращает пару ключ-значение в виде кортежа,
# а это как раз подходит нам для записи строки csv

with open('catalog.csv', 'w') as f:
    writer = csv.writer(f)
    for row in catalog.items():
        writer.writerow(row)

#Множественное число существительных
def pluralize(lst):
    return {i + 's' if lst.count(i)>1 else i for i in lst}


import os

# вывести текущую директорию
print("Текущая деректория:", os.getcwd())

#рекурсия
def rec(k):
    if (k > 0):
        result = k + rec(k - 1)
        print(result)
    else:
        result = 0
    return result

#Фибоначчи
f1,f2 = 1,1
n = int(input(''))

print(f1,f2, end=' ')

for i in range(2,n):
    f1,f2 = f2, f1 + f2
    print(f2, end=' ')
    n -= 1

#фибоначчи 2
def fib(n):
    if n < 2:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))

print(fib(9))

#Функция лямбда
def myfunc(n):
    return lambda a: a + n

my = myfunc(2)
print(my(22))

#итерация через кортеж
mytuple = ("яблоко", "банан", "вишня")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))