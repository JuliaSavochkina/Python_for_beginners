"""
* Напишите функции для методов строк через таблицу ASCII
- isdigit()
- islower()
- isalnum()
"""


def isdigit(a):
    for x in list(a):
        if ord(x) not in range(48, 58):
            k = 1
            break
        else:
            k = 0
            continue
    if k == 1:
        return False
    else:
        return True

print(isdigit('28392472'))

def islower(a):
    for x in list(a):
        if ord(x) not in range(97, 123):
            k = 1
            break
        else:
            k = 0
            continue
    if k == 1:
        return False
    else:
        return True

print(islower('djhsbfijwe'))
def isalnum(a):
    for x in list(a):
        if ord(x) not in range(48, 58) and ord(x) not in range(97, 123) and ord(x) not in range(65, 91):
            k = 1
            break
        else:
            k = 0
            continue
    if k == 1:
        return False
    else:
        return True
print(isalnum('827372AhafgjqqS'))