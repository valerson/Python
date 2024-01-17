# import pickle
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# with open('file.pkl', 'wb') as file:
#     pickle.dump(obj, file)
#
#
# import pickle
# with open('file.pkl', 'rb') as file:     # используется файл полученный на предыдущем шаге
#     obj = pickle.load(file)
#     print(obj)
#     print(type(obj))
#
#
# import pickle
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)
# print(binary_obj)
# print(type(binary_obj))
#
#
# import pickle
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)
# new_obj = pickle.loads(binary_obj)
# print(new_obj)

# import pickle
# dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}
# with open('dogs.pkl', mode='wb') as file:
#     pickle.dump(dogs, file)

# """Одинокая функция"""
# import pickle
# import sys
# def func(*args):
#     return ' '.join(args)
#
# # Сохранение функции в файл (сериализация)
# with open('func.pkl', mode='wb') as file:
#     pickle.dump(func, file)
#
# import pickle
# import sys
# file_name=input()
# with open(file_name, mode='rb') as file_pkl:
#     alone_function=pickle.load(file_pkl)
#     data=list(map(str.strip, sys.stdin))
#     print(alone_function(*data))

# """Ты не пройдешь"""
# import pickle
# def filter_dump(filename:str, object:list, typename:type):
#     result=[i for i in object if type(i) is typename]
#     with open(filename, mode='wb') as file:
#         pickle.dump(result,file)

# """Контрольная сумма"""
# import pickle
# with open('data.pkl', mode='wb') as file_pkl:
#     # temppp=['a', 'b', 3, 4, 'f', 'g', 7, 8]
#     temppp=['a', 'v', True, 1.0, '4', {}, [], [1, 2, 3], False, 'фывфы', int, (0)]
#     pickle.dump(temppp, file_pkl)
#
# """Контрольная сумма"""
# import pickle
# file_name, value=input(), int(input())
# with open(file_name, mode='rb') as file_:
#     data=pickle.load(file_)
# if type(data) is dict:
#     result=sum([i for i in data if type(i) is int])
# else:
#     temp=[i for i in data if type(i) is int]
#     if temp==[]:
#         result=0
#     else:
#         result=max(temp)*min(temp)
# print('Контрольные суммы совпадают' if value==result else 'Контрольные суммы не совпадают')

import random
print(random.choice(['салат-мимоза',
                     'свиная рулька',
                     'салат-оливье',
                     'пусть людишки думают, что у нас тут формулы какие-то']))

