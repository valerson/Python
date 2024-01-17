from datetime import datetime
my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)    # создаем полную дату-время
only_date = datetime(1560, 12, 1)                       # создаем дату-время с нулевой временной информацией
# print(my_datetime)
# print(only_date)
# print(type(my_datetime))

from datetime import date, time, datetime
my_date = date(1992, 10, 6)
my_time = time(10, 45, 17)
my_datetime = datetime.combine(my_date, my_time)

from datetime import datetime
my_datetime = datetime(2022, 10, 7, 14, 15, 45)
my_date = my_datetime.date()                     # получаем только дату (тип date)
my_time = my_datetime.time()                     # получаем только время (тип time)

from datetime import datetime
# datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС')
# my_datetime = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M:%S')
# print(my_datetime)

from datetime import datetime
datetime0 = datetime.strptime('10.08.2034 13:55:59', '%d.%m.%Y %H:%M:%S')
datetime1 = datetime.strptime('10/08/21', '%d/%m/%y')
datetime2 = datetime.strptime('Tuesday 10, August 2021', '%A %d, %B %Y')
datetime3 = datetime.strptime('18.20.34', '%H.%M.%S')
datetime4 = datetime.strptime('2021/08/10', '%Y/%m/%d')
datetime5 = datetime.strptime('10.08.2021 (Tuesday, August)', '%d.%m.%Y (%A, %B)')
datetime6 = datetime.strptime('Year: 2021, Month: 08, Day: 10, Hour: 18.', 'Year: %Y, Month: %m, Day: %d, Hour: %H.')
# print(datetime0, datetime1, datetime2, datetime3, datetime4, datetime5, datetime6, sep='\n')

from datetime import datetime
datetimes = [datetime(2022, 6, 11, 13, 26),
             datetime(2000, 12, 31, 23, 59),
             datetime(2077, 1, 1, 12),
             datetime(2042, 7, 29)]
# print(min(datetimes, key=lambda dt: dt.hour))
# print(max(datetimes, key=lambda dt: dt.year))

from datetime import datetime
text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
# print(dt)

from datetime import datetime
seconds = 2483228800
dt = datetime(2011, 11, 4)
# print(datetime.fromtimestamp(seconds))
# print(dt.timestamp())

from datetime import datetime
times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
first_half_day=[i for i in times_of_purchases if i.hour<12]
second_half_day=[i for i in times_of_purchases if i.hour>=12]
# print('До полудня' if len(first_half_day)>len(second_half_day) else 'После полудня')

from datetime import date, time, datetime
dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
result=[]
for i in range(len(dates)): result.append(datetime.combine(dates[i], times[i]))
# print(*sorted(result, key=lambda x: x.second), sep='\n')

from datetime import datetime
data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
result={int(datetime.strptime(data.get(name)[1], '%d.%m.%Y %H:%M:%S').timestamp() - datetime.strptime(data.get(name)[0], '%d.%m.%Y %H:%M:%S').timestamp()):name for name in data}
# print(result.get(min(result)))

# """Дневник космонавта 🌶️"""
# from datetime import datetime
# with open('diary.txt', 'r', encoding='utf-8') as file:
#     n,i=len(file.readlines()),0
#     file.seek(0)
#     my_dict=dict()
#
#     while i<=n:
#         temp_text=file.readline()
#         try:
#             datetime.strptime(temp_text.strip('\n'), '%d.%m.%Y; %H:%M')
#             temp_key = datetime.strptime(temp_text.strip('\n'), '%d.%m.%Y; %H:%M').timestamp()
#             my_dict[temp_key] = ''
#         except:
#             if temp_text!='\n' and i!=n:
#                 my_dict[temp_key]+=temp_text
#             if i==n:
#                 my_dict[temp_key] += temp_text +'\n'
#             i+=1
#
#     for i in sorted(my_dict):
#         print(datetime.fromtimestamp(i).strftime('%d.%m.%Y; %H:%M'))
#         print(my_dict[i])
# #КРАСИВЕ РЕШЕНИЕ ЧЕРЕЗ СЛОВАРЬ
# from datetime import datetime
# data = {}
# with open('diary.txt', encoding='utf-8') as file:
#     for i in file.read().split('\n\n'):
#         stamp = datetime.strptime(i[:17], '%d.%m.%Y; %H:%M').timestamp()
#         data[stamp] = i
# for k, v in sorted(data.items()):
#     print(v)
#     print()

"""Функция is_available_date() 🌶️"""
from datetime import datetime
def is_available_date(booked_dates: list, date_for_booking:str)->bool:
    def date_list(list_dates:list)->list:
        """
        ФОРМИРУЕМ СПИСОК ИЗ ПЕРЕДАННЫХ ДАТ
        :param list_dates:
        :return:
        """
        result_dates_list = []
        for i in list_dates:
            if '-' not in i:
                result_dates_list.append(i)
            else:
                start_day, end_day = datetime.strptime(i.split('-')[0], '%d.%m.%Y'), datetime.strptime(i.split('-')[1], '%d.%m.%Y')
                start = start_day.toordinal()
                while start <= end_day.toordinal():
                    result_dates_list.append(datetime.fromordinal(start).strftime('%d.%m.%Y'))
                    start += 1
        return result_dates_list

    booked_dates_list = date_list(booked_dates)
    date_for_booking_list=date_list([date_for_booking])
    return all([True if i not in booked_dates_list else False for i in date_for_booking_list])






