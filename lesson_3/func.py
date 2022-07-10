"""
* Напишите функции для методов строк через таблицу ASCII
- isdigit()
- islower()
- isalnum()
"""


def isdigit(a):
    number_ascii = ord(a)
    if number_ascii in range(48, 58):
        return True
    else:
        return False

print(_isdigit('r'))


def islower(a):
    number_ascii = ord(a)
    if number_ascii in range(97, 123):
        return True
    else:
        return False

print(_islower('l'))


def _isalnum(a):
    number_ascii = ord(a)
    if number_ascii in range(48, 58) or number_ascii in range(65, 91) or number_ascii in range(97,123):
        return True
    else:
        return False

print(_isalnum('='))

