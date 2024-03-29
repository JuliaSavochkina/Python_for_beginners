"""
Дан список чисел. Напишите функцию, что превратит его в список квадратов этих чисел.
"""
def to_sqr(a):
    return [x**2 for x in a]
a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(to_sqr(a))
"""
Дан произвольный список чисел. Напишите функцию, которая будет искать максимальный элемент и делить его на длину списка.
"""
def max_in_half(a: list):
    return max(a)/len(a)
a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(max_in_half(a))
"""
Даны списки:
a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
"""
def both_has(list1, list2):
    return [x for x in list2 if x in list1]
a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(both_has(a, b))
"""
* Функция to_list() принимает неограниченное количество параметров. 
Обработайте их так, чтобы на выходе получить список из этих элементов.
Поищите в сети, как подать неограниченное число аргументов
"""
def to_list(*args):
    t = []
    for i in args:
        t.append(i)
    return t

print(to_list(3, 23, 2342, 'wfwe', '1'))

