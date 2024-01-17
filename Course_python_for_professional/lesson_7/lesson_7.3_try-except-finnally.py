# try:
#     # контролируемый код
# except тип_ошибки_1:
#     # код обработки ошибки (исключения)
# except тип_ошибки_2:
#     # код обработки ошибки (исключения)
# ...
# except тип_ошибки_n:
#     # код обработки ошибки (исключения)
# else:
#     # код для случая, если ошибки (исключения) не было

# try:
#     # контролируемый код
# except тип_ошибки_1:
#     # код обработки ошибки (исключения)
# except тип_ошибки_2:
#     # код обработки ошибки (исключения)
# ...
# except тип_ошибки_n:
#     # код обработки ошибки (исключения)
# else:
#     # код для случая, если ошибки не было
# finally:
#     # код, который выполняется всегда

# def func():
#     try:
#         return 10
#     finally:
#         return 20 #сработает этот вывод
# print(func())

# """Январь, февраль, ..."""
# months = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }
# try:
#     print(months[int(input())])
# except ValueError:
#     print('Введено некорректное значение')
# except KeyError:
#     print('Введено число из недопустимого диапазона')

"""Функция add_to_list_in_dict()"""
def add_to_list_in_dict(data:dict, key:str, element):
    try:
        data[key].append(element)
    except KeyError:
        data[key]=[element]
    finally:
        return data

"""readme.txt"""
try:
    with open(input(), 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('Файл не найден')




