"""int, float"""

# Выберите два числа и возведите одно в степень другого двумя способами
num = 2
num2 = 3
print ("Task 1: ", num ** num2)
print ("Task 1: ", pow(num, num2))
# Переведите число x = 0.73 в шестнадцатиричное
print ("Task 2: ", float.hex(0.73))
# Для чисел 3.0, 8.5, 5.66 узнайте, какое из них целое
n1 = 3.0
n2 = 8.5
n3 = 5.66
print("Task 5: n1(3.0) ", n1.is_integer())
print("Task 5: n2(8.5) ", n2.is_integer())
print("Task 5: n3(5.66) ", n3.is_integer())

# переведите букву l в число ASCII
print("Task 4: ", ord('l'))