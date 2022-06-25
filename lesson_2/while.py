"""
Пользователь вводит положительные целые числа до тех пор, пока не введет 0.
Выведите максимальное введенное число (0 считать не нужно)."""

lst = []

while True:
    num = int(input('Enter a number \n(enter 0 to exit) '))
    if num >= 0:
        lst.append(num)
    else:
        print('Enter non negative number')
    if num == 0:
        lst.sort()
        print("Largest element is:", lst[-1])
        break

"""* Пользователь вводит число N. Выведите факториал число N. Факториал числа N - это произведение всех чисел от
1 до N включительно. Например, факториал числа 5 равен 120.
"""

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

i = int(input('Enter a number:'))

print("The factorial of "+ str(i) +" is: ")
print(factorial(i))
