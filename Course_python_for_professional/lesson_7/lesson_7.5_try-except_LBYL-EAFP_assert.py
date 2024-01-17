"""Пользовательские исключения"""
# class NegativeAgeError(Exception):
#     pass

# try:
#     print('Введите свой возраст')
#     age = int(input())
#     if age < 0:
#         raise NegativeAgeError('Возраст не может быть отрицательным')
#     print('Ваш возраст равен', age)
# except ValueError:
#     print('Возраст должен быть числом')
# except NegativeAgeError as e:
#     print(e)

# """Функция is_good_password() 👀"""
# def is_good_password(string:str):
#     if len(string)<9 or string.islower() or string.isupper() or sum([1 for i in string if i.isdigit()])<1 or sum([1 for i in string if i.isalpha()])<1:
#         return False
#     else:
#         return True
# print(is_good_password('МойПарольСамыйЛучший111'))

# """Функция is_good_password() 🐍"""
# class LengthError(Exception):
#     pass
# class LetterError(Exception):
#     pass
# class DigitError(Exception):
#     pass
#
# def is_good_password(string:str):
#     if len(string)<9:
#         raise LengthError()
#     if string.islower() or string.isupper() or sum([1 for i in string if i.isalpha()])<1:
#         raise LetterError()
#     if sum([1 for i in string if i.isdigit()])<1:
#         raise DigitError()
#
#     try:
#         string
#         return True
#     except (LengthError, LetterError, DigitError):
#         return False

# try:
#     print(is_good_password('Short7'))
# except Exception as err:
#     print(type(err))

# print(is_good_password('еПQSНгиfУЙ70qE'))

# try:
#     print(is_good_password('41157081231232'))
# except Exception as err:
#     print(type(err))


"""Уж лучше матрицы 😐"""
class LengthError(Exception):
    pass
class LetterError(Exception):
    pass
class DigitError(Exception):
    pass

def is_good_password(string:str):
    if len(string) < 9:
        raise LengthError('LengthError')
    if string.islower() or string.isupper() or sum([1 for i in string if i.isalpha()])<1:
        raise LetterError('LetterError')
    if sum([1 for i in string if i.isdigit()])<1:
        raise DigitError('DigitError')

# result=False
# while result!=True:
#     try:
#         is_good_password(input())
#     except Exception as err:
#         print(err)
#     else:
#         result = True
#         print('Success!')

# #некрасивый вариант
# result=False
# string=input()
# while result!=True:
#     try:
#         is_good_password(string)
#         result=True
#         print('Success!')
#     except LengthError:
#         print('LengthError')
#         result, string = False, input()
#     except LetterError:
#         print('LetterError')
#         result, string = False, input()
#     except DigitError:
#         print('DigitError')
#         result, string = False, input()


# num1 = 20
# num2 = 0
# assert num2 != 0, 'Делитель равен нулю.'
# print('Частное равно:', num1 / num2)

grade = 97
assert 0 <= grade <= 100, 'Оценка должна принадлежать отрезку [0; 100]'

file1 = 'city.jpeg'
print(file1.endswith('.jpeg'))

