"""Пользователь вводит число N. Выведите все числа от 0 до N включительно."""

N = int(input('Введите число N:'))
for numbers in range (0, N + 1):
    print(numbers)


""" Пользователь вводит числа K и N. Выведите сумму чисел от K до N включительно."""

K = int(input('Введите число K:'))
N = int(input('Введите число N:'))
s = 0
for number in range (K, N + 1):
    s += number
    print(s)

"""Пользователь вводит числа K и N. Выведите сумму только четных чисел от K до N включительно."""
K = int(input('Введите число K:'))
N = int(input('Введите число N:'))
s = 0
for numbers in range(K, N):
    if
        numbers % 2 == 0:
        s + numbers
    print(s)

""""* Напишите скрипт, что преобразует thisKindOfString в this_kind_of_string."""