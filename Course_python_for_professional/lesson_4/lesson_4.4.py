import json
countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
# print(json.dumps(countries, separators=(',',' - '), indent=3, sort_keys=True))

# import json
# words = {
#          frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#          "travel": "trævl",
#          ("hello", "world"): ("həˈləʊ", "wɜːld"),
#          "moonlight": "muːn.laɪt",
#          "sunshine": "ˈsʌn.ʃaɪn",
#          ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#          "adventure": "ədˈventʃər",
#          "beautiful": "ˈbjuːtɪfl",
#          frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#          "bicycle": "baisikl",
#          ("pilot", "fly"): ("pailət", "flai")
#         }
# data_json = json.dumps(words, skipkeys=True)
# print(data_json)

# import json
# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}
#
# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}
#
# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}
# # result=[club1,club2,club3]
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump([club1,club2,club3], file, indent=3)

import json
def is_correct_json(string:str):
    try:
        json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False

# """Элементы JSON"""
# import sys
# import json
# text=json.load(sys.stdin)
# for k,v in text.items():
#     print(f"{k}: {', '.join(map(str, v)) if type(v) is list else v}")

# """Разные типы"""
# import json
# with open('C:\\Users\\79266\\Downloads\\data.json','r', encoding='utf-8') as file:
#     text=json.load(file)
#     result=[]
#     for i in range(len(text)):
#         if type(text[i]) is str: result.append(text[i]+'!')
#         elif type(text[i]) is int or type(text[i]) is float: result.append(text[i]+1)
#         elif type(text[i]) is bool: result.append([True if text[i] is False else False][0])
#         elif type(text[i]) is list: result.append(text[i]*2)
#         elif type(text[i]) is dict:
#             text[i].update({'newkey': None})
#             result.append(text[i])
# with open('C:\\Users\\79266\\Downloads\\updated_data.json', 'w', encoding='utf-8') as file_result:
#     json.dump(result, file_result)

# #ШИКАРНОЕ РЕШЕНИЕ
# import json
# with open("data.json", "r") as json_file, open("updated_data.json", "w") as res:
#     json.dump([e + 1 if type(e) == int else e + "!" if type(e) == str else not e if isinstance(e, bool) else e + e if isinstance(e, list) else (lambda a: a | {"newkey" : None})(e) for e in json.load(json_file) if None != e], res)

# """Объединение объектов"""
# import json
# with open('C:\\Users\\79266\\Downloads\\data1.json','r', encoding='utf-8') as file_1, \
#         open('C:\\Users\\79266\\Downloads\\data2.json','r', encoding='utf-8') as file_2,\
#         open('C:\\Users\\79266\\Downloads\\data_merge.json','w', encoding='utf-8') as file_result:
#     data_1, data_2=json.load(file_1), json.load(file_2)
#     data_1.update(data_2)
#     json.dump(data_1, file_result)
#
#
# a={"Timur": 99,"Anri": 97}
# b={"Dima": 99,"Anri": 100}
# print(a|b)
#
# a.update(b)
# print(a)


# """Восстановление недостающих ключей"""
# import json
# with open('C:\\Users\\79266\\Downloads\\people.json','r', encoding='utf-8') as file_input, open('C:\\Users\\79266\\Downloads\\updated_people.json', 'w', encoding='utf-8') as file_result:
#     data_1=json.load(file_input)
#     keys=list(set([k for i in data_1 for k,v in i.items()]))
#     for i in data_1:
#         for key in keys:
#             if key not in i: i.update({key:None})
#     json.dump(data_1,file_result)


# a={'name': 'Doll', 'family_status': 'married', 'children': 'no'}
# key='abracadabra'
# a.update({key:None})
# print(a)

"""Я исповедую Python, а ты?"""
# import json
# with open('C:\\Users\\79266\\Downloads\\countries.json', 'r', encoding='utf-8') as file_input, open('C:\\Users\\79266\\Downloads\\religion.json', 'w', encoding='utf-8') as file_output:
#     #1 способ
#     data=json.load(file_input)
#     my_dict={}
#     [my_dict.setdefault(i['religion'],[]).append(i['country']) for i in data]

    #2 способ
    # data = json.load(file_input)
    # religion=set([i.get('religion') for i in data])
    # my_dict = {i:[] for i in religion}
    # for i in data:
    #     for j in religion:
    #         if i.get('religion') == j: my_dict.get(j).append(i.get('country'))

    # json.dump(my_dict,file_output, indent=3)

#КРАСИВОЕ РЕШЕНИЕ
# import json as js
#
# with open('countries.json', encoding='utf-8') as file, open('religion.json', 'w') as out:
#     d = {}
#     [d.setdefault(i['religion'], []).append(i['country']) for i in js.load(file)]
#     out = js.dump(d, out)

"""Спортивные площадки"""
# import json
# import csv
# with open('C:\\Users\\79266\\Downloads\\playgrounds.csv', 'r', encoding='utf-8') as file, open('C:\\Users\\79266\\Downloads\\addresses.json', 'w', encoding='utf-8') as file_output:
#     my_dict={}
#     [my_dict.setdefault(i['AdmArea'], {}).setdefault(i['District'],[]).append(i['Address']) for i in csv.DictReader(file, delimiter=';')]
#     json.dump(my_dict, file_output)

# """Студенты курса"""
# import json
# import csv
# with open('C:\\Users\\79266\\Downloads\\students.json', 'r', encoding='utf-8') as file, open('C:\\Users\\79266\\Downloads\\data.csv', 'w', encoding='utf-8') as file_output:
#     data=json.load(file)
#     my_list=sorted([[i['name'], i['phone']] for i in data if i['age']>=18 and i['progress']>=75], key=lambda x:x[0])
#
#     fieldnames = ['name', 'phone']
#     writer=csv.DictWriter(file_output,fieldnames=fieldnames, delimiter=',', lineterminator='\n')
#     writer.writeheader()
#     for i in my_list:
#         writer.writerow(dict(zip(fieldnames,i)))

# """Бассейны"""
# import json
# from datetime import time
# with open('C:\\Users\\79266\\Downloads\\pools.json', 'r', encoding='utf-8') as file:
#     data=json.load(file)
#     result=[]
#     for i in data:
#         [hour_start, minute_start], [hour_end, minute_end]=[j.split(':') for j in i['WorkingHoursSummer']['Понедельник'].split('-')]
#         if time(hour=int(hour_start), minute=int(minute_start)) <= time(hour=10, minute=0) and time(hour=int(hour_end), minute=int(minute_end)) >= time(hour=12, minute=0):
#             result.append([[i['DimensionsSummer']['Length'],i['DimensionsSummer']['Width']],    i['Address']])#,   i['WorkingHoursSummer']['Понедельник']    ])
#
#     for i in sorted(result, key=lambda x: (x[0][0], x[0][1]), reverse=True)[0]:
#         if type(i) is list: print(f'{i[0]}x{i[1]}')
#         else: print(i)

# """Результаты экзамена 🌶️"""
# import csv
# import json
# from datetime import datetime, date
# with open('C:\\Users\\79266\\Downloads\\exam_results.csv', 'r', encoding='utf-8') as file_input, open('C:\\Users\\79266\\Downloads\\best_scores.json', 'w', encoding='utf-8') as file_output:
#     reader=csv.DictReader(file_input, delimiter=',')
#     my_dict={}
#     for i in reader:
#         my_dict.setdefault(i['name']+' '+i['surname'], []).append(i)
#
#     result=[]
#     for k,v in my_dict.items():
#         temp=sorted(v, key=lambda x: (x['score'], x['date_and_time']), reverse=True)[0]
#         temp['score']=int(temp['score'])
#         temp['best_score'],temp['date_and_time'], temp['email']=temp.pop('score'), temp.pop('date_and_time'), temp.pop('email')
#         result.append(temp)
#
#     result=sorted(result, key=lambda x: x['email'])
#     json.dump(result,file_output, indent=3)

# """Общественное питание 😥"""
# import json
# with open('C:\\Users\\79266\\Downloads\\food_services.json', 'r', encoding='utf-8') as file:
#     data=json.load(file)
#     dict_district={}
#     dict_name_object={}
#     [dict_district.setdefault(i['District'], []).append(1) for i in data]
#     [dict_name_object.setdefault(i['OperatingCompany'], []).append(1) for i in data if i['IsNetObject']=='да']
#     dict_district=sorted({k:len(v) for k,v in dict_district.items()}.items(), key=lambda x: x[1], reverse=True)[0]
#     dict_name_object=sorted({k:len(v) for k,v in dict_name_object.items()}.items(), key=lambda x: x[1], reverse=True)[0]
#     print(f"{dict_district[0]}: {dict_district[1]}")
#     print(f"{dict_name_object[0]}: {dict_name_object[1]}")

# """Общественное питание 😰"""
# import json
# with open('C:\\Users\\79266\\Downloads\\food_services.json', 'r', encoding='utf-8') as file:
#     data=json.load(file)
#     my_dict={}
#     for i in data:
#         if my_dict.get(i['TypeObject']) is None:
#             my_dict[i['TypeObject']]=[i['Name'], int(i['SeatsCount'])]
#         else:
#             if int(i['SeatsCount']) > int(my_dict.get(i['TypeObject'])[1]):
#                 my_dict[i['TypeObject']]=[i['Name'],int(i['SeatsCount'])]
#
#     for k,v in sorted(my_dict.items()): print(f"{k}: {v[0]}, {v[1]}")




















