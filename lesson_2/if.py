"""
Пользователь вводит два целых числа. Выведите меньшее из них. """


a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
if (a < b):
    print(a)
else:
    print(b)

"""Пользователь вводит свое имя и возраст. Если возраст пользователя больше 18, то вывести строку
"Добрый вечер, name! Вы совершеннолетний, поздравляем!", иначе вывести строку "Привет, name! Приносим извинения,
но вы не можете гулять после 22:00" """


a = int(input("Сколько Вам лет? "))
name = input("Как Вас зовут? ")
if (a < 18):
    print("Привет, " + name + "! Приносим извинения,но вы не можете гулять после 22:00")
else:
    print("Добрый вечер, " + name + "! Вы совершеннолетний, поздравляем!")


"""Пользователь вводит три целых числа. Два из них равны друг другу. Выведите третье число, не равное остальным.
Если среди введенных чисел не оказалось двух равных друг другу, выведите строку "Ошибка". """

print("Введите два одинаоквых целых числа и одно число отличное от других")
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))
if (a == b):
    print("Первое и второе числа одинаковые")
elif (a == с):
    print("Первое и третье числа одинаковые")
elif (с == b):
    print("Второе и третье числа одинаковые")
else:
    print("Ошибка!")

"""Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное четное число", "нулевое число",
"положительное нечетное число", например, численным описанием числа 190 является строка "положительное четное число"."""
a = int(input("Введите целое число: "))
if (a < 0) and (a//2 == 0):
    print("отрицательное четное число")
elif (a < 0) and (a//2 != 0):
    print("отрицательное нечетное число")
elif (a > 0) and (a//2 == 0):
    print("положительное четное число")
elif (a > 0) and (a//2 != 0):
    print("положительное нечетное число")
elif (a == 0):
    print("число ноль")
else:
    print("Ошибка!")
=======

"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
"""

a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))
if (a + b > c) and (b + c > a) and (a + c > b):
    print("треугольник существует")
else:
    print("треугольник не существует")

