#Если выписать все натуральные числа меньше 10, кратные 3 или 5, 
# то получим 3, 5, 6 и 9. 
# Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
count = 0
list_1 = []

for i in range(1000):
    if (i % 5 == 0) or (i % 3 == 0):
        list_1.append(i)
        count += i
print(list_1)
print(count)