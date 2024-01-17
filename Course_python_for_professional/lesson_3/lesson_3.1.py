from datetime import date
# print(date.today())

import datetime
hurricane_andrew = datetime.date(1992, 8, 24)
# print(hurricane_andrew.weekday())

from datetime import date
florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]
early_hurricanes=0
for hurricane in florida_hurricane_dates:
    if hurricane.month <6:
        early_hurricanes += 1
# print(early_hurricanes)


from datetime import date
dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
q={1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4}
# for i in dates:
    # print(f'{i.year}-Q{q.get(i.month)}')

"""Функция get_min_max()"""
from datetime import date
def get_min_max(dates:date):
    if dates==[]: return tuple()
    else: return tuple([sorted(dates)[0], sorted(dates)[-1]])

"""Функция get_date_range()"""
from datetime import date
def get_date_range(start:date, end:date):
    result =[]
    temp_day = start.toordinal()
    while temp_day<=end.toordinal():
        result.append(start.fromordinal(temp_day))
        temp_day += 1
    return result

"""Функция saturdays_between_two_dates()"""
from datetime import date
def saturdays_between_two_dates(start:date, end:date)->int:
    """
    Функция возвращает количество суббот между датами start и end включительно.
    :param start:
    :param end:
    :return:
    """
    if start>end: step=-1
    else: step=1
    count, temp_day=0, start.toordinal()
    while temp_day>=end.toordinal() if step==-1 else temp_day<=end.toordinal():
        if date.fromordinal(temp_day).weekday()==5: count+=1
        temp_day+=step
    return count










