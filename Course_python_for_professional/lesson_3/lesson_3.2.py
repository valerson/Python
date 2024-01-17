from datetime import date, time
my_date = date(2021, 8, 10)
my_time = time(7, 18, 34)
# print(my_date)                             # вывод в ISO формате
# print(my_time)                             # вывод в ISO формате
# print(my_date.strftime('%d/%m/%y'))        # форматированный вывод даты
# print(my_date.strftime('%A %d, %B %Y'))    # форматированный вывод даты
# print(my_time.strftime('%H.%M.%S'))        # форматированный вывод времени


from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'ru-RU.UTF-8') #Русский язык
locale.setlocale(locale.LC_ALL, 'en-EN.UTF-8') #Английский язык

# from datetime import time
# alarm = time(7, 30, 25)
# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))

from datetime import date
birthday = date(1992, 10, 6)
# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))

from datetime import date, time
florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]
# присваиваем самую раннюю дату урагана в переменную first_date
# import locale
first_date = min(florida_hurricane_dates)
# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')
# print(iso)
# print(ru)
# print(us)

from datetime import date
andrew = date(1992, 8, 24)
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B(%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number

# from datetime import date, time
# day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')
# hour, minute, second = input('Введите время в формате ЧЧ:ММ:СС').split(':')
# my_date = date(int(year), int(month), int(day))        # создаем объект типа date
# my_time = time(int(hour), int(minute), int(second))    # создаем объект типа time
# print(my_date)
# print(my_time)

# from datetime import date, time
# while True:
#     try:
#         day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')
#         my_date = date(int(year), int(month), int(day))
#         print('Введена корректная дата:', my_date)
#         break
#     except ValueError:    # перехватываем ошибку типа ValueError
#         print('Введенная дата не является корректной, попробуйте еще раз')

# n = 'python'
# try:
#     n = int(n)
#     print(n * 2)
# except ValueError:
#     print('Произошла ошибка')

# """Две даты"""
# from datetime import date
# data_1, data_2=list(map(int, input().split('-'))), list(map(int, input().split('-')))
# date(data_1[0], data_1[1], data_1[2])
# print(min([date(data_1[0], data_1[1], data_1[2]), date(data_2[0], data_2[1], data_2[2])]).strftime('%d-%m (%Y)'))

"""Отсортированные даты"""
# from datetime import date
# my_list = [list(map(int, input().split('-'))) for i in range(int(input()))]
# my_list_1=sorted([date(i[0], i[1], i[2]).toordinal() for i in my_list])
# print(*[date.fromordinal(i).strftime('%d/%m/%Y') for i in my_list_1], sep='\n')

"""Функция print_good_dates()"""
from datetime import date
def print_good_dates(dates:list)->date:
    """
    Функция выводит «интересные» даты в порядке возрастания, каждую на отдельной строке,
    в формате  month_name DD, YYYY, где month_name — полное название месяца на английском.
    :param dates: list
    :return: date
    """
    result=[]
    for i in dates:
        if int(i.strftime('%Y')) == 1992 and ((int(i.strftime('%m')) + int(i.strftime('%d')))==29):
            result.append(i)
    result=sorted([i.toordinal() for i in result])
    print(*[date.fromordinal(i).strftime('%B %d, %Y') for i in result], sep='\n')

"""Функция is_correct()"""
from datetime import date
def is_correct(day:int, month: int, year:int)->bool:
    """
    Функция возвращает True, если дата с компонентами day, month и year является корректной,
    или False в противном случае.
    :param day:
    :param month:
    :param year:
    :return:
    """
    try:
        date(year, month, day).toordinal()
        return True
    except ValueError:
        return False

"""Корректные даты"""
date_input, count=input(), 0
while date_input!='end':
    temp = list(map(int, date_input.split('.')))
    day, month, year = temp[0], temp[1], temp[2]
    if is_correct(day, month, year):
        print('Корректная')
        count+=1
    else: print('Некорректная')
    date_input=input()
print(count)








