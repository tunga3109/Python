birthday = int(input('Сколько тебе лет? '))
count = birthday//5
if birthday >= 21:
    print('Ты совершеннолетний даже в Америке')
elif birthday >= 21:
    print('Ты совершеннолетний даже в странах СНГ')
count = 0
if birthday < 5:
    print('Юбилеев не было')
else:
    for year in range(5,birthday+1,5):
        count += 1
    print('Кол-во юбилеев: ',count)
