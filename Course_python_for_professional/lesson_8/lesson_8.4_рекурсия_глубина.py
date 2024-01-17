def get_all_str(data):
    if type(data) == str:
        print(data, end=' ')            # базовый случай
    if type(data) == list:
        for i in data:
            get_all_str(i)              # рекурсивный случай



def find_key(data, key):
    if key in data:
        return data[key]  # базовый случай

    for v in data.values():
        if type(v) == dict:
            value = find_key(v, key)  # рекурсивный случай
            if value is not None:
                return value

# info = {'name': 'Alyson',
#         'surname': 'Hannigan',
#         'birthday': {'day': 24, 'month': 'March', 'year': 1974},
#         'family': {'parents': {'mother': 'Emilie Posner', 'father': 'Alan Hannigan'}}}
#
# print(find_key(info, 'year'))
# print(find_key(info, 'father'))

"""Функция recursive_sum()"""
def recursive_sum(nested_lists,summ=0):
    if type(nested_lists) is int:
        return nested_lists
    if type(nested_lists) is list:
        for i in nested_lists:
            summ+=recursive_sum(i)
    return summ

# my_list = [1, 2,[4,3]]
# print(recursive_sum(my_list))

"""Функция linear()"""
def linear(nested_lists):
    def func(nested_lists, my_list=[]):
        if type(nested_lists) is not list:
            my_list.append(nested_lists)
        elif type(nested_lists) is list:
            for i in nested_lists:
                func(i)
        return my_list
    return func(nested_lists)

# my_list = [3, [4], [5, [6, [7, 8]]]]
# print(linear(my_list))
#
# my_list = [3, [4], [5, [6, [7, 8]]]]
# print(linear(my_list))


"""Функция get_value()"""
def get_value(nested_dicts, key):
    result=''
    if key in nested_dicts:
        return str(nested_dicts[key])
    else:
        for k, value in nested_dicts.items():
            if type(value) is dict:
                result+=get_value(value, key)
        return result

# """Функция get_all_values() 🌶️"""
# def get_all_values(nested_dicts, key):
#     result=[]
#     def func(nested_dicts, key, result):
#         value=nested_dicts.get(key)
#         if value is not None:
#             result.append(value)
#
#         for k, value in nested_dicts.items():
#             if type(value) is dict:
#                 func(value, key,result)
#         return result
#
#     return set(func(nested_dicts,key,result))

#ЕЩЕ ВАРИАНТ. КРАСИВЕЕ И ПРОЩЕ
# def get_all_values(nested_dicts, key):
#     result = set()  # создаем пустое множество для хранения найденных значений
#     if key in nested_dicts:  # если ключ найден, добавляем его значение в результат
#         result.add(nested_dicts[key])
#     for value in nested_dicts.values():  # перебираем все значения словаря
#         if isinstance(value, dict):  # если значение является словарем, вызываем рекурсивно функцию для этого словаря
#             result.update(get_all_values(value, key))
#     return result

"""Функция dict_travel() 🌶️🌶️"""
def dict_travel(nested_dicts):
    def func(nested_dicts, my_dict=dict()):
        if len(nested_dicts)==1:
            for k,v in nested_dicts.items():
                # базовый случай словарь из одного элемента
                if type(v) is not dict:
                    my_dict.update({k:v})
                else:
                    new_dict = {f'{k}.{list(v.keys())[i]}': list(v.values())[i] for i in
                                range(len(list(v.keys())))}
                    func(new_dict)

        else:
            for key,value in nested_dicts.items():
                if isinstance(value, dict):
                    # print('AUHHHH')
        #             # print(list(value.keys()))
        #             # print(list(value.values()))
                    new_dict={f'{key}.{list(value.keys())[i]}':list(value.values())[i] for i in range(len(list(value.keys())))}
                    func(new_dict)
        #             pass
                else:
                    func(dict([(key,value)]))

        return my_dict
    for k, v in sorted(func(nested_dicts).items()):
        print(f'{k}: {v}')


#КРАСИВОЕ РЕШЕНИЕ!!!!!
def dict_travel(data):
    for k, v in sorted(data.items()):
        if isinstance(v, dict):
            dict_travel({f'{k}.{key}': val for key, val in v.items()})
        else:
            print(f'{k}: {v}')

# data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
# dict_travel(data)

print(1**1)

