"""** Напишите валидатор email. Проверьте, что
- есть символ собачки
- строка непустая
- что в имени пользователя нет пробелов
- что доменное имя существует ('aero', 'arpa', 'asia', 'biz', 'cat', 'com', 'coop', 'edu', 'gov', 'info', 'int', 'jobs', 'mil', 'mobi', 'museum', 'name', 'net', 'org', 'pro', 'tel', 'travel')
В случае успеха верните True иначе - False
"""


def is_valid_email(email):
    domains = ('aero', 'arpa', 'asia', 'biz', 'cat', 'com', 'coop', 'edu', 'gov', 'info', 'int', 'jobs', 'mil', 'mobi', 'museum', 'name', 'net', 'org', 'pro', 'tel', 'travel')
    if email and ' ' not in email and '@' in email and email.index('@') != 0:
        for domain in domains:
            if domain in email:
                return True
    else:
        return False


print(is_valid_email("w@com"))