from collections import ChainMap
empty_chain_map = ChainMap()                      # создаем пустой ChainMap объект
# print(empty_chain_map)
numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}
chain_map = ChainMap(numbers, letters)            # создаем ChainMap объект на основе словарей numbers и letters
# print(chain_map)


# from collections import ChainMap
# for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
# vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}
# pets = ChainMap(for_adoption, vet_treatment)
# print(pets['dogs'])
# print(pets['cats'])
# print(pets['pythons'])
# print(pets['tigers'])


# from collections import ChainMap
# numbers = {'one': 1, 'two': 2}
# letters = {'a': 'A', 'b': 'B'}
# alpha_num = ChainMap(numbers, letters)
# for key in alpha_num:
#     print(key, '->', alpha_num[key])


# from collections import ChainMap
# letters = ChainMap({'a': 'A'}, {'b': 'B', 'c': 'C'})
# letters['b'] = 'BB'
# letters['c'] = 'CC'
# print(letters)

from collections import ChainMap
letters = ChainMap({'a': 'A', 'b': 'B'},
                   {'c': 'C'},
                   {'d': 'D', 'e': 'E'})
letters.clear()
# print(letters)


# from collections import ChainMap
# fruits = ChainMap({'kiwi': 10, 'banana': 20},
#                   {'lime': 10, 'pineapple': 15},
#                   {'kiwi': 15, 'lime': 5})
# print(*fruits.values())

# """Зоопарк"""
# from collections import ChainMap
# import json
# with open('C:\\Users\\79266\\Downloads\\zoo.json', 'r', encoding='utf-8') as file:
#     text=json.load(file)
#     result=ChainMap(*text)
#     itog=sum([i for i in result.values()])
#     print(itog)

"""Булочный магнат"""
from collections import ChainMap, Counter
bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

total_dict=dict(ChainMap(bread, meat, sauce, vegetables, toppings))
text=sorted(input().split(','))
result_order=Counter(text)
n=len(max(result_order, key=len))

result_price, max_len=0,0
for k,v in result_order.items():
    print_str=f"{k.ljust(n+1,' ')}x {v}"
    print(print_str)
    result_price+=v*total_dict.get(k)
    if len(print_str)>max_len: max_len=len(print_str)
print_str=f"ИТОГ: {result_price}р"
if len(print_str)>max_len: max_len=len(print_str)
print('-'*max_len)
print(print_str)



