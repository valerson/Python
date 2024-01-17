from datetime import timedelta

delta1 = timedelta(days=5) + timedelta(seconds=3600)  # 5 дней + 1 час
delta2 = timedelta(days=5) - timedelta(seconds=3600)  # 5 дней - 1 час
# print(delta1)
# print(delta2)

from datetime import timedelta


def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60


delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)
hours, minutes = hours_minutes(delta)
# print(delta)
# print(hours)
# print(minutes)

from datetime import timedelta

delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
# print('Количество дней =', delta.days)
# print('Количество секунд =', delta.seconds)
# print('Количество микросекунд =', delta.microseconds)
# print('Общее количество секунд =', delta.total_seconds())

# delta1 = timedelta(seconds=57)
# print(type(delta1))
# print(delta1 == 57)

# Рассмотрим следующую задачу: рабочая смена длится 7 часов 30 минут, сколько полных смен в 3-х сутках?
from datetime import timedelta

all_time = timedelta(days=3)
smena = timedelta(hours=7, minutes=30)
# print(all_time // smena)
# print(all_time % smena)

# from datetime import datetime
# release = datetime(2022, 7, 15)
# today = datetime(2022, 7, 5)
# print(release - today)

from datetime import timedelta

td = timedelta(weeks=-1, hours=-20, minutes=-120)
abs_td = abs(td)
# print(td)
# print(abs_td)

from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))

from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)
days = abs(today - birthday)
# print(days.days)

from datetime import datetime, timedelta
# day=datetime.strptime(input(), '%d.%m.%Y')
# day_next, day_previous=day+timedelta(days=1), day-timedelta(days=1)
# print(day_previous.strftime('%d.%m.%Y'), day_next.strftime('%d.%m.%Y'), sep='\n')

from datetime import datetime, timedelta
# h,m,s=list(map(int, input().split(':')))
# print(timedelta(hours=h, seconds=(m*60+s)).seconds)

from datetime import time, timedelta
# h,m,s=list(map(int, input().split(':')))
# n=int(input())
# result = timedelta(hours=h, seconds=(m*60+s+n))
# hour, minute=result.seconds//3600, (result.seconds//60)%60
# print(f'{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(result.seconds-hour*3600-minute*60).zfill(2)}')

from datetime import date, timedelta


def num_of_sundays(year: int) -> int:
    result = []
    temp = [date(year, 1, i) for i in range(1, 8) if date(year, 1, i).isoweekday() == 7][0]
    while temp <= date(year, 12, 31):
        result.append(temp)
        temp = temp + timedelta(weeks=1)
    return len(result)


# """Продуктивность"""
# from datetime import datetime, timedelta
# temp_day=datetime.strptime(input(), '%d.%m.%Y')
# work=[]
# for i in range(1, 11):
#     work.append(temp_day.strftime('%d.%m.%Y'))
#     temp_day+=timedelta(days=1+len(work))
# print(*work, sep='\n')

"""Соседние даты"""
# from datetime import datetime, timedelta
# date_list=list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), input().split()))
# print([abs((date_list[i] - date_list[i-1]).days) for i in range(1, len(date_list))])

from datetime import timedelta, datetime


def fill_up_missing_dates(dates: list) -> list:
    """
    Функция возвращает список, в котором содержатся все даты из списка dates,
    расположенные в порядке возрастания, а также все недостающие промежуточные даты.
    :param dates:
    :return:
    """
    list_dates = sorted(list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dates)))
    temp, last = list_dates[0], list_dates[-1]
    while temp != last:
        if temp not in list_dates: list_dates.append(temp)
        temp += timedelta(days=1)
    return [i.strftime('%d.%m.%Y') for i in sorted(list_dates)]


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
# print(fill_up_missing_dates(dates))

"""Реп по матеше"""
# from datetime import datetime, timedelta
# start_time = datetime.strptime(input(), '%H:%M')
# end_time = datetime.strptime(input(), '%H:%M')
# while (start_time+timedelta(minutes=45))<=end_time:
#     print(f"{start_time.strftime('%H:%M')} - {(start_time+timedelta(minutes=45)).strftime('%H:%M')}")
#     start_time+=timedelta(minutes=55)

from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]
result = sum([(datetime.strptime(i[1], '%H:%M') - datetime.strptime(i[0], '%H:%M')).seconds for i in data])
# print(int(result/60))

"""Пятница, 13-е"""
# from datetime import datetime, date, timedelta
# # start_date, end_date=date(1,1,1), date(28,12,31)
# # start_date, end_date=date(9968,1,1), date(9995,12,31)
# # start_date, end_date=date(28*3,1,1), date(28*4,12,31)
# # start_date, end_date=date(9996,1,1), date(9999,12,31)
# start_date, end_date=date(1,1,1), date(9999,12,31)
# day_of_weeks=[0,0,0,0,0,0,0]
# while start_date<end_date:
#     if start_date.day==13:
#         day_of_weeks[start_date.weekday()]+=1
#     start_date+=timedelta(days=1)
# print(*day_of_weeks, sep='\n')

# """Снова не успел"""
# from datetime import date, timedelta, time, datetime
#
# work_time = {'0': (time(9, 0), time(21, 0)), '1': (time(9, 0), time(21, 0)), '2': (time(9, 0), time(21, 0)),
#              '3': (time(9, 0), time(21, 0)), '4': (time(9, 0), time(21, 0)), '5': (time(10, 0), time(18, 0)),
#              '6': (time(10, 0), time(18, 0))}
# date_now, time_now = input().split()
# date_now = datetime.strptime(date_now, '%d.%m.%Y').date()
# time_now = datetime.strptime(time_now, '%H:%M').time()
# if work_time.get(str(date_now.weekday()))[1] > time_now and time_now >= work_time.get(str(date_now.weekday()))[0]:
#     print(work_time.get(str(date_now.weekday()))[1].hour * 60 + work_time.get(str(date_now.weekday()))[
#         1].minute - time_now.hour * 60 - time_now.minute)
# else:
#     print('Магазин не работает')

# """Самое понятное условие"""
# from datetime import date, timedelta, time, datetime
# start_day=datetime.strptime(input(),'%d.%m.%Y')
# end_day=datetime.strptime(input(),'%d.%m.%Y')
# while start_day<end_day:
#     if (int(start_day.month) + int(start_day.day))%2==0: start_day += timedelta(days=1)
#     else: break
# while start_day<=end_day:
#     if start_day.isoweekday()!=1 and start_day.isoweekday()!=4: print(start_day.strftime('%d.%m.%Y'))
#     start_day+=timedelta(days=3)

# """Сотрудники организации 😄"""
# from datetime import date, timedelta, time, datetime
# my_dict=dict()
# count=1
# for i in range(int(input())):
#     text=input().split()
#     if my_dict.get(datetime.strptime(text[2], '%d.%m.%Y').date()) is not None:
#         count+=1
#     my_dict[datetime.strptime(text[2], '%d.%m.%Y').date()] = text[0] + ' ' + text[1]
# print(min(my_dict).strftime('%d.%m.%Y'), my_dict.get(min(my_dict)) if count==1 else count)

# """Сотрудники организации 🙂"""
# from datetime import date, datetime, time, timedelta
# my_dict=dict()
# for i in range(int(input())):
#     text=input().split()
#     if my_dict.get(datetime.strptime(text[2], '%d.%m.%Y').date()) is not None:
#         my_dict[datetime.strptime(text[2], '%d.%m.%Y').date()]=my_dict.get(datetime.strptime(text[2], '%d.%m.%Y').date())+1
#     else:
#         my_dict[datetime.strptime(text[2], '%d.%m.%Y').date()] = 1
# maximum=sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[0][1]
# for k,v in sorted(my_dict.items()):
#     if v==maximum: print(k.strftime('%d.%m.%Y'))

# """Сотрудники организации 😔"""
# from datetime import date, datetime, time, timedelta
# #создаем список текущая дата + 7 дней
# date_now=datetime.strptime(input(), '%d.%m.%Y')
# date_now_list=[date_now + timedelta(days=i) for i in range(1,8)]
# # print(date_now_list)
#
# #создаем словарь дата рождения имя фамилия
# my_dict=dict()
# for i in range(int(input())):
#     text=input().split()
#     my_dict[text[0]+' '+text[1]] = datetime.strptime(text[2], '%d.%m.%Y')
#
# result='Дни рождения не планируются'
# for k,v in sorted(my_dict.items(), key=lambda x: x[1]):
#     for i in date_now_list:
#         if v.replace(year=i.year) == i:
#             result=k
#             break
#
# print(result)

"""FAKE NEWS 🌶️"""
from datetime import date, time, timedelta, datetime
def choose_plural(amount: int, declensions: tuple)->str:
    """

    Функция возвращает строку, полученную путем объединения подходящего
    существительного из кортежа declensions и количества amount, в следующем формате:
    <количество> <существительное>

    :param amount:
    :param declensions:
    :return:
    """
    if amount >= 100:
        temp = amount % 100
    else:
        temp = amount

    if temp == 1:
        return f'{amount} {declensions[0]}'
    elif temp == 2 or temp == 3 or temp == 4:
        return f'{amount} {declensions[1]}'
    elif 20 >= temp >= 5:
        return f'{amount} {declensions[2]}'

    elif 99 > temp > 20:
        if str(temp)[-1] == '1':
            return f'{amount} {declensions[0]}'
        elif str(temp)[-1] in '234':
            return f'{amount} {declensions[1]}'
        elif str(temp)[-1] in '567890':
            return f'{amount} {declensions[2]}'

death_line=datetime(year=2022, month=11, day=8, hour=12, minute=00, second=00)
temp_now=input().split()
datetime_now=datetime.combine(datetime.strptime(temp_now[0], '%d.%m.%Y').date(), datetime.strptime(temp_now[1], '%H:%M').time())

dict_time={'day': ('день','дня','дней'), 'hours': ('час','часа','часов'), 'minute':('минута','минуты','минут')}
day, hour, minute= (death_line-datetime_now).days, (death_line-datetime_now).seconds//3600, ((death_line-datetime_now).seconds//60)%60

if day<0 or datetime_now==death_line: print('Курс уже вышел!')

elif day!=0 and hour!=0: print(f"До выхода курса осталось: {choose_plural(int(day),dict_time['day'])} и {choose_plural(int(hour), dict_time['hours'])}")
elif day!=0 and hour==0: print(f"До выхода курса осталось: {choose_plural(int(day),dict_time['day'])}")

elif day==0 and hour!=0 and minute!=0: print(f"До выхода курса осталось: {choose_plural(int(hour), dict_time['hours'])} и {choose_plural(int(minute), dict_time['minute'])}")
elif day==0 and hour!=0 and minute==0: print(f"До выхода курса осталось: {choose_plural(int(hour), dict_time['hours'])}")
elif day==0 and hour==0 and minute!=0: print(f"До выхода курса осталось: {choose_plural(int(minute), dict_time['minute'])}")








