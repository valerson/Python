# try:
#     nums = [10, 5, 20, 25]
#     print(nums[100])
# except (KeyError, IndexError) as err:    # записываем сгенерированное исключение в переменную err
#     print('URAA')
#     print(err)
#     print(type(err))


# from sys import exc_info
# try:
#     х = 1 / 0
# except Exception as err:
#     print(exc_info())

# try:
#     raise IndexError('ошибочка')             # возбуждение исключения вручную
# except Exception as err:
#     print(err)
#     print(type(err))

# def get_month_name(index):
#     if not index.isdigit():
#         raise TypeError('Аргумент должен быть числом.')
#     if int(index) < 1 or int(index) > 12:
#         raise ValueError('Аргумент должен быть целым числом от 1 до 12.')
#      ...

# try:
#     x, y = 10, 0
#     if y == 0:
#         raise ZeroDivisionError('Произошло деление на ноль.')
# except ZeroDivisionError as err:
#     print(err)
#     print(err.args)
#     print(type(err.args))

# try:
#     х = 1 / 0
# except Exception as err:
#    raise ZeroDivisionError('Описание исключения') from err

# try:
#     х = 1 / 0
# except Exception as err:
#     print(err)                  # каким-то образом обработали перехваченное исключение
#     raise                       # пробрасываем исключение выше

# try:
#     raise ValueError('Произошла ошибка')
# except ValueError as e:
#     print(e)

"""Функция get_weekday()"""
def get_weekday(number):
    week = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье", }
    if type(number) is not int:
        raise TypeError('Аргумент не является целым числом')
    if number>7 or number<=0:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')

    return week[number]


"""Функция get_id()"""
def get_id(names:list, name:str):
    if type(name) is not str:
        raise TypeError('Имя не является строкой')
    if name[0]!=name[0].upper() or name[1:]!=name[1:].lower() or sum([1 for i in name if i.isalpha()])!=len(name):
        raise ValueError('Имя не является корректным')
    names.append(name)
    return len(names)

# """Десериализация"""
# import json
# file_name=input()
# try:
#     with open(file_name, 'r', encoding='utf-8') as file:
#         print(json.load(file))
# except FileNotFoundError:
#     print('Файл не найден')
# except json.decoder.JSONDecodeError:
#     print('Ошибка при десериализации')

#ПРАВИЛЬНОЕ РЕШЕНИЕ
# import json
# try:
#     try:
#         with open(input(), encoding='utf-8') as file:
#             data = json.load(file)
#             print(data)
#     except FileNotFoundError:
#         raise FileNotFoundError('Файл не найден')
#     except json.decoder.JSONDecodeError:
#         raise json.decoder.JSONDecodeError('Ошибка при десериализации')
# except Exception as err:
#     print(err)






