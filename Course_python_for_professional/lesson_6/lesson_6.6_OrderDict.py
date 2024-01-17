# my_dict={'one':1, 'two':2, 'tree':3}
# my_dict['four']=4
# print(my_dict)
# del my_dict['tree']
# print(my_dict)
# my_dict['tree']=3
# print(my_dict)


# from collections import OrderedDict
# numbers = OrderedDict(one=1, two=2, three=3)
# print(numbers)
# numbers.move_to_end('one')       # last=True
# print(numbers)
# numbers.move_to_end('three', last=False)       # last=False
# print(numbers)
"""last (необязательный аргумент) – логическое значение (тип bool), которое определяет, 
в какой конец словаря мы перемещаем элемент, 
значение True (по умолчанию) перемещает элемент в конец, значение False – в начало"""

from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)
# for key in sorted(letters):
# letters.move_to_end(key)
# print(letters)


# from collections import OrderedDict
# numbers = OrderedDict(one=1, two=2, three=3)
# print(numbers.popitem())
# print(numbers)
# print(numbers.popitem(last=False))
# print(numbers)
"""Если методу popitem() передать необязательный аргумент last=False, 
то он начнет удалять и возвращать элементы в порядке FIFO"""

from collections import OrderedDict
# letters = OrderedDict(b=2, d=4, a=1, c=3)
# letters.sorted_keys = lambda: sorted(letters.keys())

# print(letters)
# print(letters.sorted_keys())
# letters['e'] = 5
# print(letters)
# print(letters.sorted_keys())
# for key in letters.sorted_keys():
#     print(key, '->', letters[key])

# from collections import OrderedDict
# vector = OrderedDict(x=3, y=4, module=5)
# print(*reversed(vector))

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
new_data = OrderedDict()
for k, v in data.items():
    new_data[k] = v
    new_data.move_to_end(k, last=False)
# print(new_data)

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
new_data = OrderedDict()
list_1=list(data.keys())
list_2=list_1[::-1]
i=0
while i<=len(data)/2:
    new_data[list_1[i]]=data[list_1[i]]
    new_data[list_2[i]] = data[list_2[i]]
    i+=1
# print(new_data)

"""Функция custom_sort() 🌶️"""
from collections import OrderedDict
def custom_sort(ordered_dict:OrderedDict, by_values:bool=False)->OrderedDict:
    for k, v in sorted(ordered_dict.items(), key=lambda x: x[1] if by_values else x[0]):
        ordered_dict.move_to_end(k, last=True)

    # if by_values:
    #     #сортировка по значениям
    #     for k,v in sorted(ordered_dict.items(), key=lambda x: x[1]):
    #         ordered_dict.move_to_end(k, last=True)
    # else:
    #     #сортировка по ключам
    #     for i in sorted(ordered_dict):
    #         ordered_dict.move_to_end(i, last=True)

    return ordered_dict


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)



