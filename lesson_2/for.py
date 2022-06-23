"""
Пользователь вводит число N. Выведите все числа от 0 до N включительно.
"""
n = int(input("Введите число N: "))
for x in range(n + 1):
    print(x)

"""
Пользователь вводит числа K и N. Выведите сумму чисел от K до N включительно.
"""
k = int(input("Введите число K: "))
n = int(input("Введите число N: "))
s = 0
for x in range(k, n + 1):
    s = x + s
print(s)

"""Пользователь вводит числа K и N. Выведите сумму только четных чисел от K до N включительно.

"""
k = int(input("Введите число K: "))
n = int(input("Введите число N: "))
s = 0
if k % 2 == 0:
    k = k
else:
    k = k + 1
for x in range(k, n + 1, 2):
    s = x + s
print(s)

"""
* Напишите скрипт, что преобразует thisKindOfString в this_kind_of_string.
"""
str = 'thisKindOfString'
clean_str = ''
for s in str:
    if s.isupper():
        s = '_' + s.lower()
    clean_str += s
print(clean_str)


