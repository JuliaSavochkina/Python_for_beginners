"""int, float"""

# Выберите два числа и возведите одно в степень другого двумя способами
# -- способ 1
a = 5
b = 7
c = a**b
print(c)
# -- способ 2
d = pow(a, b)
print(d)

# Переведите число x = 0.73 в шестнадцатиричное
x = int(0.73)
e = hex(x)
print(e)

# Для чисел 3.0, 8.5, 5.66 узнайте, какое из них целое

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False
print(is_integer_num(3.0)) # true
print(is_integer_num(8.5)) # false
print(is_integer_num(5.66)) # false

# переведите букву l в число ASCII

find_ascii_of_character = ord('l')
print(find_ascii_of_character)

