"""
Дана строка. Выполните преобразования над ней.
"""

s = '  svGHytr  TYUijthHG  '

# Подсчитайте количество символов t в строке
s = '  svGHytr  TYUijthHG  '
print(s.count('t'))


# Проверьте входит ли подстрока 'tyu' в строку
s = '  svGHytr  TYUijthHG  '
result = 'tyu' in s
print(result)



# Проверьте, состоит ли строка только из заглавных букв
s = '  svGHytr  TYUijthHG  '
result = s. isupper()
print(result)


# Удалите пробелы до и после слов строки

s = '  svGHytr  TYUijthHG  '
print(s.strip())



# * Удалите все пробелы из строки и сделайте первую букву заглавной

s = '  svGHytr  TYUijthHG  '
x = s.replace(' ', "")
print(x.capitalize())




# ** Дана строчная латинская буква, переведите ее в заглавную без использования втрокового метода



# ** Cложите строку «5» и число 5. Чтобы на выходе получилось число. Не используя операция int().


a = '5'
b = 5
f = (repr(b))
res_str = str(f) + a
print(res_str)

