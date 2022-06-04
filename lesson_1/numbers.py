"""int, float"""

# Выберите два числа и возведите одно в степень другого двумя способами
# 1 способ:
x = 10
y = 3
print(x**y)

# 2 способ:
a = 5
b = 3
import math
f = math.pow (5, 3)
print(f)


# Переведите число x = 0.73 в шестнадцатиричное
x = 0.73
b = (x).hex()
print(b)


# Для чисел 3.0, 8.5, 5.66 узнайте, какое из них целое

str = (3.0).is_integer()
print(str)

str = (8.5).is_integer()
print(str)

str = (5.66).is_integer()
print(str)



# переведите букву l в число ASCII

str = "l"
result = ord(str)
print(result)

