# from collections import defaultdict
# a='mississipi'
# my_dict=defaultdict(int)
# for i in a:
#     my_dict[i]+=1
# print(dict(my_dict))
# print(my_dict)

from collections import Counter
counter = Counter('mississippi')     # создаем счетчик на основе строки
# print(counter)


from collections import Counter
letters = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# print(letters)
# letters.update('missouri')
# print(letters)
# print(*letters)

from collections import Counter
vegetables = Counter({'cabbage': 10, 'pepper': 'seven', 'pumpkin': 'four'})
vegetables.update({'cabbage': 5, 'pepper': 'two'})
# print(vegetables['pepper'])
# print(vegetables['cabbage'])

from collections import Counter
clothes = Counter([('shirt', 3), ('dress', 1), ('shirt', 3)])
# print(clothes)

from collections import Counter
files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
         'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
         'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
         'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
         'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
         'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
         'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
         'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
         'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
         'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
         'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
         'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
         'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
temp=[i.split('.')[1] for i in files]
my_dict=Counter(temp)
# for k,v in sorted(my_dict.items(), key=lambda x: x[0]):
#     print(f"{k}: {v}")


"""Функция count_occurences()"""
from collections import Counter
def count_occurences(word:str, words:str)->int:
    my_dict=Counter(list(map(lambda x: x.lower(), words.split())))
    return my_dict[word.lower()]

word = 'python'
words = 'Python Conferences python training python events'
# print(count_occurences(word, words))

"""Не поленимся и запишем"""
from collections import Counter
# for k,v in sorted(Counter(input().split(',')).items(), key=lambda x:x[0]):
#     print(f"{k}: {v}")

"""А сколько стоит курс?"""
# from collections import Counter
# text=input().split(',')
# len_max=max([len(i) for i in text])
# for k,v in sorted(Counter(text).items(), key=lambda x:x[0]):
#     result=sum([ord(i) for i in k.replace(' ','')])
#     print(f"{k.ljust(len_max,' ')}: {result} UC x {v} = {result*v} UC")

"""The Zen of Python"""
from collections import Counter
with open('C:\\Users\\79266\\Downloads\\pythonzen.txt', 'r', encoding='utf-8') as file:
    my_dict=Counter()
    for i in file.readlines():
        my_dict.update(''.join([j for j in i.lower().strip() if j.isalpha()]))
    for k,v in sorted(my_dict.items(), key=lambda x:x[0]):
        print(f"{k}: {v}")






