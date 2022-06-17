"""
Пользователь вводит положительные целые числа до тех пор, пока не введет 0. Выведите максимальное введенное число (0 считать не нужно)."""

count = 0
list = []
while True:
    n = int(input('Введите число: '))
    count += 1
    list.append(n)
    if n == 0:
        break
print(max(list))

"""* Пользователь вводит число N. Выведите факториал число N. Факториал числа N - это произведение всех чисел от
1 до N включительно. Например, факториал числа 5 равен 120.
"""
number = int(input('Введите число: '))
factorial = 1
while number > 1:
    factorial = factorial * number
    number = number - 1
print(factorial)