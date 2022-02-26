# Задача 1
s = [1, 4, ['hello', 'name', 12], 'age', 12.3, 135.0]
for s1 in s:
    print(s1)
    print(type(s1))

# Задача 2
li = input('Введите эллементы списка: ').split()
print(li)
for e in range(0, len(li)-1, 2):
    li[e], li[e + 1] = li[e + 1], li[e]
    print(li)

# # задача 3
season = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'sumer': [6, 7, 8], 'autumn': [9, 10, 11]}
month = int(input('Введите месяц  в виде целого числа: '))
for el in season:
    if month in season[el]:
        print(el)

# задача 4
from typing import List

a = input('Введите слова: ').split()
for el, i  in enumerate(a, 1):
    print(el, i)
    if len(i) > 10:
        i = i[0 : 10]
        print(el , i)