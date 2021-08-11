example = []  # или example = list() или example = [1,2,3]
print(example)
example.append(1)  # добавляет элемент в список
print(example)
example1 = [2, 3, 4]
example.extend(example1)  # добавляет список в список
print(example)
example.insert(2, 5)  # добавляет 5 на позицию 2 (человеческое 3)
print(example)
example.remove(3)  # удаляет первый элемент со значением 3
print(example)
try:
    print(example.remove(200))  # вернёт ValueError, так как такого элемента в списке нет
except ValueError:
    print("Ошибочка((")
example.pop(2)  # если цифры нет удаляет последний элемент
print(example)
print(example.index(4))  # возвращает индекс элемента с этим значением также можно указать диапазон,
# в котором функция должна искать этот элемент example.index(4, 0, 3)
# функция print пишется только для того, чтобы показать вам, что возвращает функция внутри
example.extend(example1)
print(example.count(3))  # посчитает количество элементов в списке со значением 3
example.sort()  # сортирует элементы списка, также параметром в этот метод можно прописать фукнцию, которая возвращает 1, -1 или 0
print(example)
example.reverse()
print(example)
example1 = example.copy()  # копирует список в другой список, создаёт новый список example1
print(example1)
example1 = example  # копирует указатель на example
example1.remove(3)  # удаляет элемент со значением 3
print(example)
import copy
example1 = copy.deepcopy(example)  # используйте, если example - это список списков или словарь со списками или словарями
print(example1)
example.clear()
print(example)

