from collections import Counter
letters = Counter('mississippi')
numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])
# print(letters.most_common())
# print(numbers.most_common())
#
# print(letters.most_common(2))
# print(numbers.most_common(3))

from collections import Counter
letters = Counter('mississippi')
numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])
# print(list(letters.elements())) #обязательно ЛИСТ. методы выводит итератор, а не список
# print(list(numbers.elements()))

from collections import Counter
letters = Counter(i=4, s=4, a=0, p=2, b=-98, m=1)
# print(list(letters.elements()))


from collections import Counter
counter1 = Counter(i=4, s=40, a=1, p=20, b=98, z=69)
counter2 = Counter(i=2, s=20, a=6, p=12, m=1, z=69)
counter1.subtract(counter2)       # обновляем значения в counter1
# print(counter1)


from collections import Counter
counter1 = Counter(i=10, s=40, p=10, m=1)
counter2 = Counter(i=2, s=8, p=10, m=3)
# print(counter1 + counter2)
# print(counter1 - counter2)
# print(counter2 - counter1)


from collections import Counter
counter = Counter(green=10, red=25, blue=5)
# print(counter.__dict__)
counter.__dict__['min_value'] = lambda: min(counter.values())
counter.max_value = lambda: max(counter.values())
# print(counter.min_value())
# print(counter.max_value())


from collections import Counter
counter1 = Counter(a=2, b=3, c=6)
counter2 = Counter(a=5, b=7, c=1)
# print(counter1-counter2)

# from collections import Counter
# letters1 = Counter(a=1, b=-2, c=3, d=-4)
# letters2 = +letters1
# letters3=-letters2
# print(letters3)

# from collections import Counter
# letters1 = Counter('stepik')
# letters2 = {'s': 1, 't': 1, 'e': 1, 'p': 1, 'i': 1, 'k': 1}
# print(letters1+letters2)

"""В поисках слов 😇"""
from collections import Counter
# text=list(map(lambda x:x.lower(), input().split()))
# print(sorted(dict(Counter(text)).items(), key=lambda x:x[1], reverse=True)[0][0])
# print(Counter(text).most_common(1)[0][0])

# """В поисках слов 😋"""
# from collections import Counter
# temp=Counter(list(map(lambda x:x.lower(), input().split()))).most_common()
# print(*sorted([i[0] for i in temp if i[1]==temp[-1][1]]), sep=', ')

"""В поисках слов 🥳"""
# from collections import Counter
# text=Counter(list(map(lambda x:x.lower(), input().split()))).most_common()
# print(sorted([i[0] for i in text if i[1]==text[0][1]], reverse=True)[0])

# """Статистика длин слов"""
# from collections import Counter
# text=sorted(Counter(list(map(lambda x: len(x), input().split()))).items(), key=lambda x: x[1])
# for i in text:
#     print(f"Слов длины {i[0]}: {i[1]}")

"""Все еще достоин"""
from collections import Counter
import sys
# a=[i.strip().split() for i in sys.stdin]
# print(sorted(a, key=lambda x: int(x[1]))[1][0])

# c = Counter()
# for data in sys.stdin:
#     name, score = data.split()
#     c.update({name: int(score)})
# print(c.most_common()[-2][0])


from collections import Counter
data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
data.min_values=lambda: [i for i in data.most_common() if i[1]==min(data.values())]
data.max_values=lambda: [i for i in data.most_common() if i[1]==max(data.values())]
# print(data.min_values())
# print(data.max_values())


# """Here we go again"""
# from collections import Counter
# import csv
# with open('C:\\Users\\79266\\Downloads\\name_log.csv', 'r', encoding='utf-8') as file:
#     my_list = [i['email'] for i in csv.DictReader(file)]
#     # for k,v in sorted(Counter(my_list).items(), key=lambda x: x[0]):
#     #     print(f"{k}: {v}")
#     print(*[f"{k}: {v}" for k,v in sorted(Counter(my_list).items(), key=lambda x: x[0])], sep='\n')

"""Функция scrabble()"""
from collections import Counter
def scrabble(symbol:str,word:str):
    result=Counter(symbol.lower())
    result.subtract(Counter(word.lower()))
    # return False if result.most_common()[-1][1]<0 else True
# scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek')

    #КРАСИВОЕ РЕШЕНИЕ!!!
    # return Counter(word.lower()) <= Counter(symbols.lower())

# """Функция print_bar_chart()"""
# from collections import Counter
# def print_bar_chart(data, mark):
#     n=max(list(map(lambda x:len(x), Counter(data).keys())))
#     n=len(max(Counter(data), key=len))
#
#     print(*[f'{k.ljust(len(max(Counter(data), key=len)) + 1, " ")}|{v*mark}' for k,v in sorted(Counter(data).items(), key=lambda x: x[1], reverse=True)], sep='\n')

"""Бесплатные курсы берут свое 😢"""
import csv
import json
from collections import defaultdict
with open('C:\\Users\\79266\\Downloads\\prices.json', 'r', encoding='utf-8') as price_file:
    price=json.load(price_file)


#сделали из всех файлов с продажами один словарь с количеством проданного товара суммарно за год
my_dict=defaultdict(list)
directory='C:\\Users\\79266\\Downloads\\'
name=['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']
for i in name:
    with open(directory+i, 'r', encoding='utf-8') as file:
        sales=csv.reader(file)
        #пропускаем одну строку (заголовок файла)
        next(sales, None)
        [my_dict[row[0]].extend(row[1:]) for row in sales]
for k,v in my_dict.items():
    my_dict[k]=sum(list(map(int, v)))

result=0
for k,v in price.items():
    my_dict[k]=my_dict.get(k)*int(v)
    result+=my_dict.get(k)
# print(result)


"""Бесплатные курсы берут свое 😭"""
from collections import Counter
books=Counter(list(map(int, input().split())))
result=0
for i in range(int(input())):
    buyers=input().split()
    if books.get(int(buyers[0]),0) != 0:
        books[int(buyers[0])]=books.get(int(buyers[0]))-1
        result+=int(buyers[1])
print(result)


