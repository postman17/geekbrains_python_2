class UsernameLenError(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return 'Имя пользователя {} должно быть меньше 26 символов'.format(self.username)


class ResponseCodeError(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return 'Неверный код ответа {}'.format(self.code)


class ResponseCodeLenError(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return 'Неверная длина кода {}. Длина кода должна быть 3 символа.'.format(self)


class MandatoryKeyError(Exception):
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return 'Не хватает обязательного атрибута {}'.format(self.key)


class AccountNameNotStr(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Account_name {} не является строкой.'.format(self.name)


class ResponseNotDict(Exception):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        return 'Response {} не является словарем.'.format(self.response)