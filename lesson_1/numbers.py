"""int, float"""

# Выберите два числа и возведите одно в степень другого двумя способами
a = 3
b = 6
print(a**b)
print(pow(a, b))

# Переведите число x = 0.73 в шестнадцатиричное
x = 0.73
print(float.hex(x))


# Для чисел 3.0, 8.5, 5.66 узнайте, какое из них целое
d = 3.0
e = 8.5
f = 5.66
print(d.is_integer(), e.is_integer(), f.is_integer())

# переведите букву l в число ASCII
print(ord('l'))