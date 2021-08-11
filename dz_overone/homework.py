# import random
#
#
# count = int(input("Введите количество участников: "))
# names = []
# for i in range(count):
#     names.append(input("Введите имя: "))
# names.sort()
# score = dict.fromkeys(names, 0)
# print(score)
# while True:
#     bullet = random.randint(1, 6)
#     p = 0
#     names = []
#     for key in score.keys():
#         names.append(key)
#     print(names)
#     while len(names) > 1:
#         for name in names[p:]:
#             choice = int(input(name + ", крути барабан: "))
#             if choice == bullet:
#                 p = names.index(name)
#                 score.update({name: score.get(name) + 1})
#                 print(name + ", ты выбыл")
#                 names.remove(name)
#                 bullet = random.randint(1, 6)
#                 break
#             else:
#                 print("Выжил")
#         else:
#             p = 0
#
#     print(str(names) + ", ты победил")
#     cont = input("Продолжаем?[Д, Н]")
#     if cont.lower() == "н":
#         break
#
#
# for key, value in score.items():
#     if value == min(score.values()):
#         print("Больше всех умер: ", key, value)
#     if value == max(score.values()):
#         print("Меньше всех умер: ", key, value)



# spisok = [1, 2, 2, 3, 4, 5, 4, 6]
# spisok.sort()
# for i in spisok:
#     if spisok.count(i) < 2:
#         print(i)

# import random
#
# kort = ("орёл", "решка")
# attempts = []
# attempt = 1
# while True:
#     rand = random.choice(kort)
#     answer = input("Орёл или решка?")
#     if answer == "0":
#         break
#     elif answer.lower() != rand:
#         print("Неправильно, ещё раз")
#         attempt += 1
#     else:
#         print("Молодец")
#         attempts.append(attempt)
#         attempt = 1
#
# print("Минимальное количество попыток "+str(min(attempts)))
# print("Максимальное количество попыток " + str(max(attempts)))


letters = {"G": "П", "H": "Р", "B": "И", "D": "В", "T": "Е", "N": "Т"}
line = input("Напишите привет на английской раскладке:")
for key in enumerate(letters.keys()):
    if key[1] != line[key[0]].upper():
        print("Неверно")
        break
else:
    print("Всё круто")
