#  Множества – это неупорядоченные наборы простых объектов. Они необходимы тогда, когда присутствие объекта в наборе важнее порядка или того, сколько раз данный объект
#  там встречается.
#  Используя множества, можно осуществлять проверку принадлежности, определять, является ли данное множество подмножеством другого множества, находить пересечения
#  множеств и так далее.

count = ['Бразилия', 'Россия', 'Индия', 'Индия']  # Множество можно объявить несколькими способами
check2 = ['Бразилия', 'Россия', 'Индия', 'Индия', "4"]
countries = set(count)  # первый из них, при объявлении в множестве не останется повторяющихся элементов
print(countries)  # здесь при выводе вы не увидите Индию ещё раз
# countries = {'Бразилия', 'Россия', 'Индия'}  # также множество можно объявить просто использовав фигурные скобочки
# также до того 3.5 версии корректно было написать
# countries = set(['Бразилия', 'Россия', 'Индия', 'Индия'])  # однако сейчас такую строчку вам будет подчёркивать, как ошибку
# почему? потому что запись с фигурными скобочками выполняется в 2 раза быстрее и в этом нет смысла
print(len(countries))  # число элементов в множестве (размер множества).
s = "Россия"
if s in countries:
    print("Россия есть")  # точно так же, как и со списками или строками это работает

check = ("Привет", "Пока")
for_union = set(check)
print(countries.isdisjoint(count))  # True, если set и count не имеют общих элементов.
print(countries.isdisjoint(check))  # здесь, можно использовать любые итерируемые объекты
check = ("Привет", "Пока", "Россия")
print(countries == count)  # все элементы countries принадлежат count, все элементы count принадлежат countries.
print(countries.issubset(count))  # или countries <= count - все элементы countries принадлежат count.
print(countries.issuperset(check2))  # или countries >= check2 - аналогично в другую сторону.
print(countries.union(for_union))  # или countries | for_union | ... - объединение нескольких множеств.
print(countries.intersection(for_union))  # или countries & for_union & ... - пересечение.
print(countries.difference(for_union))  # или countries - for_union - ... - множество из всех элементов set, не принадлежащие ни одному из other.
print(countries.symmetric_difference(for_union))  # countries ^ for_union - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
copy = countries.copy()  # копия множества.
print(copy)

# И операции, непосредственно изменяющие множество:
for_update1 = {1, 2, 3, 4}
for_update2 = {4, 5, 6}
for_update1.update(for_update2)  # for_update1 |= for_update2 | ... - объединение.
print(for_update1)
for_update1 = {1, 2, 3, 4}
for_update1.intersection_update(for_update2)  # for_update1 &= for_update2 & ... - пересечение.
print(for_update1)
for_update1 = {1, 2, 3, 4}
for_update1.difference_update(for_update2)  # for_update1 -= for_update2 | ... - вычитание.
print(for_update1)
for_update1 = {1, 2, 3, 4}
for_update1.symmetric_difference_update(for_update2) # for_update1 ^= for_update2 - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
print(for_update1)
for_update1.add(7)  # добавляет элемент в множество.
print(for_update1)
for_update1.remove(7)  # удаляет элемент из множества. KeyError, если такого элемента не существует.
print(for_update1)
for_update1.discard(3)  # удаляет элемент, если он находится в множестве.
print(for_update1)
for_update1.pop()  # удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
print(for_update1)
for_update1.clear()  # очистка множества.
print(for_update1)
