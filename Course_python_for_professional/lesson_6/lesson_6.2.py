# """Я и сам своего рода переводчик"""
# my_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# result=dict(zip(my_list, list(input())))
# for i in list(input().lower()): print(result[i] if i in my_list else i, end='')
# #КРАСИВЫЙ ВЫВОД НА ПЕЧАТЬ
# print(reslt.get(i, i), end='')


import collections
Point = collections.namedtuple('Point_name', ['x', 'y']) #по сути это point_name=(x,y) только дальше можно присваивать x и y значения
# p=Point(x=1, y=2) # создаем именованный кортеж Point
p = Point(3, 7) #равносильно


# print(p)
# print(p.x)
# print(p.y)

x=collections.namedtuple('chto_to', ['a', 'b', 'c'])
new_tuple=x(a='abc', b=1, c=[1,2,3])
x.a='bvc'
# new_tuple.a='bvs'
# print(x.a)
#
# new_tuple=x(a=3)
# print(new_tuple) #выдаст ошибку, потому что кортеж неизменяемый
# new_tuple.c.append(6)
# print(new_tuple)

# from collections import namedtuple
# headers = ('name', 'surname', 'age', 'class')
# Student = namedtuple('Student', headers, rename=True) #Python автоматически переименовал поле class в _3.
# stud = Student('Роман', 'Белых', 26, 10)
# print(stud)

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'], defaults=(0, 0))
point1 = Point()      # используем значения по умолчанию
point2 = Point(1, 9)
# print(point1)
# print(point2)

from collections import namedtuple
Movie = namedtuple('Movie', ['name', 'genres', 'director', 'imdb_rating'])
movie = Movie('La La Land', ['comedy', 'drama', 'musical'], 'Damien Chazelle', 8)
# print(movie['name'])

from collections import namedtuple
Weather = namedtuple('Weather', ['temp', 'wind', 'rain', 'cloud'])
tokyo_weather = Weather(11, 6, 0.0, 25)
print(Weather.temp)
print(tokyo_weather.temp)

