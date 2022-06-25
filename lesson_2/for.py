"""
Пользователь вводит число N. Выведите все числа от 0 до N включительно.
"""

num = int(input('Enter number:'))
i = 0
for i in range(i, num+1):
    print(i)

"""
Пользователь вводит числа K и N. Выведите сумму чисел от K до N включительно.
"""

list = []
num1 = int(input('Enter number1:'))
num2 = int(input('Enter number2:'))
for i in range(num1, num2+1):
    list.append(i)
print(sum(list))

"""
Пользователь вводит числа K и N. Выведите сумму только четных чисел от K до N включительно."""

list = []
num1 = int(input('Enter number1:'))
num2 = int(input('Enter number2:'))
for i in range(num1, num2+1):
    if (i % 2) == 0:
        list.append(i)
print(sum(list))

"""
* Напишите скрипт, что преобразует thisKindOfString в this_kind_of_string.
"""
text = 'thisKindOfString'
new_text = ''

for i, letter in enumerate(text):
    if i and letter.isupper():
        new_text += '_'

    new_text += letter
new_text = new_text.lower()
print(new_text)
