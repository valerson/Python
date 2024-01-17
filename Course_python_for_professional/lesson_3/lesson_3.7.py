# import calendar, locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# for name in calendar.day_name:
#     print(name)

# import calendar
"""Функция setfirstweekday() позволяет изменить поведение по умолчанию
и устанавливает заданный день недели в качестве начала недели."""
# calendar.setfirstweekday(calendar.SUNDAY)     # эквивалентно
# calendar.setfirstweekday(6)

import calendar
"""Функция month(year, month, w=0, l=0) возвращает календарь на месяц в многострочной строке.
Аргументами функции являются: year (год), month (месяц), w (ширина столбца даты) 
и l (количество строк, отводимые на неделю)."""
# print(calendar.month(2021, 9))
# print(calendar.month(2021, 10))
# print(calendar.month(2021, 9, w=3))
# print(calendar.month(2021, 9, l=2))
# print(calendar.month(2021, 9, w=5, l=2))

# import calendar
# month = calendar.month_name[12]
# print(month)

# import calendar
# print(*[calendar.isleap(year=int(input())) for i in range(int(input()))], sep='\n')

# import calendar
# text=input().split()
# print(calendar.month(int(text[0]), [i for i in range(1,13) if text[1]==calendar.month_abbr[i]][0]))

# import calendar
# year, month, day=list(map(int, input().split('-')))
# print(calendar.day_name[calendar.weekday(year, month, day)])

# import calendar
# year, month = input().split()
# print(calendar.monthrange(int(year), [i for i in range(1,13) if month==calendar.month_name[i]][0])[1])

import calendar
from datetime import datetime, date
def get_days_in_month(year: int, month:str)->list:
    month_dict={'January':1, 'February':2, 'March':3,
                'April':4, 'May':5, 'June':6,
                'July':7, 'August':8, 'September':9,
                'October':10, 'November':11, 'December':12}
    month_number=month_dict.get(month)
    return [date(year,month_number, i) for i in range(1, calendar.monthrange(year, month_number)[1]+1)]


# import calendar
# from datetime import timedelta, datetime
# def get_all_mondays(year:int)->list:
#     star_day, result=datetime(year, 1, 1),[]
#     while star_day<=datetime(year,12,31):
#         mont, day=star_day.month, star_day.day
#         if calendar.weekday(year, mont, day)==0: result.append(star_day.date())
#         star_day+=timedelta(days=1)
#     return result

import calendar
from datetime import timedelta, datetime
def ermitag_for_free(year:int)->dict:
    star_day, result=[datetime(year, 1, i) for i in range(1,8) if calendar.weekday(year,1,i)==3][0],dict()

    while star_day<=datetime(year,12,31):
        month, day=star_day.month, star_day.day
        if result.get(month)==None: result[month]=[star_day.date().strftime('%d.%m.%Y')]
        else: result.get(month).append(star_day.date().strftime('%d.%m.%Y'))
        star_day+=timedelta(days=7)
    return result
for k,v in ermitag_for_free(int(input())).items(): print(v[2])









