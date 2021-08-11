#1-ое задание
while True:
    number = input('Введите 7-значное число: ')
    #проверяем длину введенного пользоватем число и является ли число
    if len(number) == 7 and number.isdigit():
        even_numbers = []
        odd_numbers = []
        for num in number:
            if int(num) % 2 == 0:
                even_numbers.append(num)
            elif int(num) % 2 == 1:
                odd_numbers.append(num)
        print(even_numbers)
        print(odd_numbers)


    if len(even_numbers) > len(odd_numbers):
        odd_sum = 0
        for even_num in even_numbers:
            odd_sum += int(even_num)
        print('Сумма четных чисел:', odd_sum)
    elif len(odd_numbers) > len(even_numbers):
        print('Произведение 1-го,3-го и 6-го цифр:', int(number[0]) * int(number[2]) * int(number[5]))


#2-ое задание
while True:
    word = input('Введите слово или текст: ').lower()
    word = word.replace(' ','')
    vowels = ['a','e','o','u','y','i']
    if word.isalpha():
        count_vowels = 0
        count_consonant = 0
        for letter in word:
            if letter in vowels:
                count_vowels += 1
            elif letter not in vowels:
                count_consonant += 1
            else:
                print('Ошибка') 
        if count_consonant == count_vowels:
            print('кол-во гласных и согласных одинаковы!')
            print(vowels)
            

        print('кол-во гласных:', count_vowels)
        print('кол-во согласных:', count_consonant)   
    else:
        print('Вы не ввели слово ')  

#3-е задание
import random

score_random = 0
score_num = 0
for i in range(7):
    num_1 = int(input('Введите первое число(от 1 до 20): '))
    num_2 = int(input('Введите второе число(от 1 до 20): '))

    random_num_1 = random.randint(1,21)
    random_num_2 = random.randint(1,21)

    if 0 < num_1 < 21 and 0 < num_2 < 21:
        if num_1 + num_2 > random_num_1 + random_num_2:
            score_num += 1
        elif random_num_1 + random_num_2 > num_1 + num_2:
            score_random + 1
    else:
        print('Введите число от 1 до 20')


print(score_num)
print(score_random)


#4-ое задание
import random

times = int(input('Кол-во чисел: '))
find_num = input('Какую цифру в числе будем искать(от 1 до 9): ')

for i in range(times):
    random_num = random.randint(1,1000000)
    random_num = str(random_num)
    num_list = []
    if 0 < int(find_num) < 10:
        for num in random_num:
            num_list.append(num)
    
    print('В числе ',random_num, ' цифра', find_num ,'встречается', num_list.count(find_num),' раз')

#5-ое задание
write = input('Введи что-нибудь: ')
numbers = []
for elem in write:
    if elem.isdigit():
        numbers.append(elem)

print('Все числа, которые встречаются в строке - ',numbers)


#6-ое задание
word = input('Введи что-нибудь: ')
word = word.replace(' ','')
upper = []
lower = []
index = 0
vowels = ['a','e','o','u','y','i']

if word.isalpha():
        count_vowels = 0
        count_consonant = 0
        for letter in word.lower():
            if letter in vowels:
                count_vowels += 1
            elif letter not in vowels:
                count_consonant += 1
            else:
                print('Ошибка')

for letters in word:
    pair = word[index:index+2]
    if pair.isupper() and len(pair) == 2:
        upper.append(pair)
    elif pair.islower() and len(pair) == 2:
        lower.append(pair)    
    index += 1

print('Кол-во пар верхнего регистре: ', len(upper))
print('Кол-во пар нижнего регистре: ', len(lower))

print('кол-во гласных:', count_vowels)
print('кол-во согласных:', count_consonant) 


