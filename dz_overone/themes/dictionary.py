example = {"Единица": 1, "Двойка": 2}
#example = dict.fromkeys(['1', '2'])
#example = dict([(1, 2), (2, 3)])


example1 = example.copy()  # - возвращает копию словаря.
print(example1)

print(example.get("Единица"))  # - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

print(example.items())  # - возвращает пары (ключ, значение).
for key, value in example.items():
    print(str(key)+" Ключ")
    print(str(value) + " Значение")

print("Ключи")
print(example.keys())  # - возвращает ключи в словаре.

print("Удаление последнего")
print(example.popitem())  # удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.


example.setdefault(5)  # - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).
print(example)


example.update({5: 6})  # - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
print(example)

print("Значения")
print(example.values())  # - возвращает значения в словаре.

example.clear()  # - очищает словарь.
print(example)
