from collections import ChainMap
for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}
pets = ChainMap(for_adoption, vet_treatment)
# print(pets)
pets.maps.append({1:2, 3:4})
# print(pets.maps)
del pets.maps[0]
# print(pets)
# print(type(pets.maps))

# pets.maps.reverse()
# pets.maps[0]['lions'] = 10
# del pets.maps[1]['cats']
# print(pets)
# print(pets.maps)


# for animals in pets.maps:
#     for key, value in animals.items():
#         print(key, '->', value)


# from collections import ChainMap
# dad = {'name': 'Timur', 'age': 29}
# mom = {'name': 'Rosaly', 'age': 28}
# old_family = ChainMap(dad, mom)
# son = {'name': 'Soslan', 'age': 0}
# new_family = old_family.new_child(son)
# print(old_family)
# print(new_family)



# from collections import ChainMap
# dad = {'name': 'Timur', 'age': 29}
# mom = {'name': 'Rosaly', 'age': 28}
# old_family = ChainMap(dad, mom)
# new_family = old_family.new_child()
# print(old_family)
# print(new_family)

# from collections import ChainMap
# dad = {'name': 'Timur', 'age': 29}
# mom = {'name': 'Rosaly', 'age': 28}
# son = {'name': 'Soslan', 'age': 0}
# family = ChainMap(son, dad, mom)
# print(family)
# print(family.parents)
# print(type(family.parents))



# from collections import ChainMap
# fruits = ChainMap({'apple': 10, 'banana': 20},
#                   {'lemon': 10, 'pineapple': 15},
#                   {'kiwi': 15, 'lime': 5})
#
# fruits.maps.append({'mango': 20, 'melon': 20})
# print(fruits)
# del fruits.maps[0]
# del fruits.maps[1]
# print(fruits)

# from collections import ChainMap
# chainmap = ChainMap()
# print(chainmap.maps)

"""Функция get_all_values()"""
from collections import ChainMap
def get_all_values(chainmap:ChainMap, key)->set:
    result=set([i.get(key) for i in chainmap.maps])
    result.discard(None)
    return result

"""Функция deep_update()"""
from collections import ChainMap
def deep_update(chainmap: ChainMap, key:str, value:str):

    count=0
    for dict_chainmap in chainmap.maps:
        if dict_chainmap.get(key) is not None:
            count+=1
            dict_chainmap[key]=value
    # print(len(chainmap))
    # if len(chainmap)
    if count==0: chainmap.maps[0][key]=value

    return None

# chainmap = ChainMap({})
# deep_update(chainmap, 'city', 'Moscow')
# print(chainmap)
#
# chainmap = ChainMap({})
# print(deep_update(chainmap, 'city', 'Moscow'))


"""Функция get_value()"""
# from collections import ChainMap
# def get_value(chainmap:ChainMap, key:str, from_left:bool=True):
#     if from_left:
#         for i in chainmap.maps:
#             if i.get(key)!=None:
#                 return i.get(key)
#                 break
#         return None
#     else:
#         for i in chainmap.maps[::-1]:
#             if i.get(key) != None:
#                 return i.get(key)
#                 break
#         return None

#ХОРОШЕЕ РЕШЕНИЕ!!!
from collections import ChainMap
def get_value(chainmap, key, from_left=True):
    if not from_left:
        chainmap.maps.reverse()
    return chainmap.get(key)



chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})

print(get_value(chainmap, 'name'))