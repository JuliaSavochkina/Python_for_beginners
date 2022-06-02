"""int, float"""

# Выберите два числа и возведите одно в степень другого двумя способами
a = 4
b = 7
print(a**b)
print(pow(a, b))

# Переведите число x = 0.73 в шестнадцатиричное

x = int(0.73)
print (x)
print(hex(x))

# Для чисел 3.0, 8.5, 5.66 узнайте, какое из них целое
q = 3.0
w = 8.5
e = 5.66
print(q.is_integer(), w.is_integer(), e.is_integer())

# переведите букву l в число ASCII
d = 'l'
print(ord(d))