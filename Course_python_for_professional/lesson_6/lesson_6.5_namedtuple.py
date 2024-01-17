from collections import defaultdict

info = defaultdict(int)  # создаем словарь со значением по умолчанию 0
info['name'] = 'Timur'
info['age'] = 29
info['job'] = 'Teacher'
# print(info['salary'])
# print(info)

"""для int – число 0
для float – число 0.0
для bool – значение False
для str – пустая строка ''
для list – пустой список []
для tuple – пустой кортеж ()
для set – пустое множество set()
для dict – пустой словарь {}"""

# from collections import defaultdict
# info1 = defaultdict(int, name='Timur', age=29, job='Teacher')
# info2 = defaultdict(int, [('name', 'Timur'), ('age', 29), ('job', 'Teacher')])
# print(info1)
# print(info2)

# from collections import defaultdict
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# result = defaultdict(int)
# print(result)
# for num in numbers:
#     result[num] += 1
# print(result)

# from collections import defaultdict
# my_dict = defaultdict(list)
# for i in range(7):
#     my_dict[i].append(i)
# for key in my_dict:
#     print(key, my_dict[key])

# from collections import defaultdict
# info = defaultdict(lambda: '1000000$', {'name': 'Timur', 'age': 29, 'job': 'Teacher'})
# print(info['name'])
# print(info['salary'])

# !!!!!!!!!Функцию, которая возвращает значение по умолчанию для отсутствующих ключей,
# можно явно менять через атрибут default_factory
from collections import defaultdict
# data = defaultdict(int)
# print(data['salary1'])
# data.default_factory = list
# print(data['salary2'])
# data.default_factory = float
# print(data['salary3'])
# data = defaultdict(None)
# data=defaultdict(None)
# print(data['name'])


# from collections import defaultdict
# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
# my_dict=defaultdict(int)
# for i in data: my_dict[i[0]]+=i[1]
# for k,v in sorted(my_dict.items()): print(f'{k}: ${v}')

# from collections import defaultdict
# staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'), ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'), ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'), ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'), ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'), ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'), ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]
# my_dict=defaultdict(int)
# for i in staff:
#     my_dict[i[0]]+=1
# for k,v in sorted(my_dict.items()):
#     print(f'{k}: {v}')


from collections import defaultdict

staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
                ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
                ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
                ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
                ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
                ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
                ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
                ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
                ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
                ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
                ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
                ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
                ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
                ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
                ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
                ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
                ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
                ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
                ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
                ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
                ('Accounting', 'Dale Houston')]
# my_dict = defaultdict(dict)
# for i in sorted(staff_broken, key=lambda x: x[1]):
#     my_dict[i[0]].update({i[1]:1})
# for k,v in sorted(my_dict.items()):
#     print(f"{k}: ", end='')
#     print(*[i for i in list(v.keys())], sep=', ')

#2 ВАРИАНТ через МНОЖЕСТВО
# my_dict=defaultdict(set)
# for i in sorted(staff_broken):
#     my_dict[i[0]].add(i[1])
# # print(my_dict)
# for k,v in my_dict.items():
#     print(f"{k}: {', '.join(sorted(list(v)))}")

# """Функция wins()"""
# from collections import defaultdict
# def wins(pairs:list)->defaultdict:
#     my_dict=defaultdict(set)
#     for i in pairs:
#         my_dict[i[0]].add(i[1])
#     return my_dict
# result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))


"""Функция flip_dict()"""
from collections import defaultdict
def flip_dict(dict_of_lists:dict)->defaultdict:
    my_dict=defaultdict(list)
    for k,v in dict_of_lists.items():
        for j in v:
            my_dict[j].append(k)
    return my_dict


# flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]})
# print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

"""Функция best_sender()"""
from collections import defaultdict
def best_sender(messages:list, senders:list):
    my_tuple_list=[(senders[i], messages[i]) for i in range(len(messages))]
    my_dict=defaultdict(int)
    for i in my_tuple_list:
        my_dict[i[0]]+=len(i[1].split())
    print(sorted(my_dict.items(), key=lambda x: (x[1],x[0]), reverse=True).keys()[0][0])





