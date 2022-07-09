"""
* Напишите функции для методов строк через таблицу ASCII
- isdigit()
- islower()
- isalnum()
"""


def _isdigit(a):
    number_ascii = ord(a)
    if number_ascii in range(48, 58):
        return True
    else:
        return False

print(_isdigit(str('w')))


def _islower(a):
    number_ascii = ord(a)
    if number_ascii in range(97, 123):
        return True
    else:
        return False


print(_islower('a'))


def _isalnum(a):
    number_ascii = ord(a)
    if number_ascii in range(48, 58) or number_ascii in range(97, 123) or number_ascii in range(65,91):
        return True
    else:
        return False


print(_isalnum('&'))



# s = 'thisKindOfString'
# new_s = ''
# for letter in s:
#     if letter.isupper():
#         new_letter = letter.lower()
#         new_letter_with_symbol = f'_{new_letter}'
#         new_s += new_letter_with_symbol
#     else:
#         new_s += letter
# print(new_s)
#
# def cc_string_to_underscored_string(s):
#   pass
#
# def cc_string_to_underscored_string(s):
#     new_s = ''
#     for letter in s:
#         if letter.isupper():
#             new_letter = letter.lower()
#             new_letter_with_symbol = f'_{new_letter}'
#             new_s += new_letter_with_symbol
#         else:
#             new_s += letter
#     return new_s
#
# print(cc_string_to_underscored_string('thisKindOfString'))
# print(cc_string_to_underscored_string('sayHello'))
# print(cc_string_to_underscored_string('myNameIsJhon'))


