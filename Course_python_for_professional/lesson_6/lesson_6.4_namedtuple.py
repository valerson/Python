# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height', 'четвертый_с_пробелом'], defaults=(1,2,3,4))
# tim = Person('Тимур', 29, 170)
# print(tim)
# print(tim._fields)
# print(Person._field_defaults)

from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'height'])
ExtendedPerson = namedtuple('ExtendedPerson', [*Person._fields, 'weight'])  # распаковка полей старого кортежа
# timur = ExtendedPerson('Тимур', 29, 170, 65)
# print(timur)
# print(ExtendedPerson._fields)
# timur_2=Person('Тим',10, 156)
# print(timur_2)
# print(timur_2._fields)

# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height'])
# timur = Person('Тимур', 29, 170)
# for field, value in zip(Person._fields, timur):
#     print(field, '->', value)

import collections
my_tuple=collections.namedtuple('my_tuple_new', ['x_1', 'x_2', 'x_3'])
# a=(11,22,99)
b=[10,20,30]
# # result=my_tuple(a[0],a[1],a[2])
# # result=my_tuple(*b)
# result=my_tuple(*a)
# print(result)

import collections
my_tuple=collections.namedtuple('my_tuple_new', ['x_1', 'x_2', 'x_3'])
# b=[10,20,30]
# result=my_tuple(*b) #создаем именованный кортеж способ 1
# # print(result)
result=my_tuple._make(b) #создаем именованный кортеж способ 2
# print(result)
# print(*result)
# print(my_tuple._fields)

# my_dict=result._asdict() #делаем из именованного кортежа словарь
# # print(my_dict)
# result_2=result._replace(x_1=999, x_2=888) #создает новый именованный кортеж с заменой части
# print(result)
# print(result_2)
# result=result._replace(x_1=999, x_2=888) #создает новый именованный кортеж с заменой части
# print(result)

# from collections import namedtuple
# PcHardware = namedtuple('PcHardware', 'cpu,gpu,motherboard,ram', defaults=[None, None])
# print(PcHardware._field_defaults)
# print(PcHardware._fields)

# a={'devicetype': 'keyboard', 'model': 'Logitech G213'}
# print(*a)
# print(**a)

from collections import namedtuple
Fruit=namedtuple('Fruit', ['name','color','vitamins'])

from collections import namedtuple
Game = namedtuple('Game', 'name developer publisher')
ExtendedGame = namedtuple('ExtendedGame', [*Game._fields,'release_date', 'price'])


# from collections import namedtuple
# import pickle
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
# with open('C:\\Users\\79266\\Downloads\\data.pkl', mode='rb') as pik:
#     for i in pickle.load(pik):
        #1 СПОСОБ ПЕЧАТИ (ПЛОХОЙ)
        # print(f"{Animal._fields[0]}: {i.name}\n"
        #       f"{Animal._fields[1]}: {i.family}\n"
        #       f"{Animal._fields[2]}: {i.sex}\n"
        #       f"{Animal._fields[3]}: {i.color}\n")

        # 2 СПОСОБ ПЕЧАТИ (ХОРОШИЙ)
        # for k,v in zip(Animal._fields, i):
        #     print(f'{k}: {v}')
        # print('')

        # 3 СПОСОБ ПЕЧАТИ (ХОРОШИЙ)
        # for k,v in i._asdict().items():
        #     print(f'{k}: {v}')
        # print()



from collections import namedtuple
User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

# plan_priority = ['Gold', 'Silver', 'Bronze', 'Basic']
# for i in sorted(users, key=lambda x: (plan_priority.index(x.plan), x.email)):
#     print(f'{i.name} {i.surname}\n  Email: {i.email}\n  Plan: {i.plan}\n')

"""Вы кто такие? Я вас не звал"""
import csv
from datetime import datetime, date, time
from collections import namedtuple
with open('C:\\Users\\79266\\Downloads\\meetings.csv', 'r', encoding='utf-8') as file:
    reader=csv.DictReader(file)
    # for i in sorted(reader, key=lambda x: datetime.strptime(x['meeting_date']+' '+x['meeting_time'],'%d.%m.%Y %H:%M')):
    #     print(i['surname'], i['name'])

    # Friends=namedtuple('Friends', ['surname','name','meeting_date','meeting_time'])
    # meeting=[Friends(**i) for i in reader]
    # for i in sorted(meeting, key=lambda x: datetime.strptime(x.meeting_date+' '+x.meeting_time,'%d.%m.%Y %H:%M')):
    #     print(i.surname, i.name)








