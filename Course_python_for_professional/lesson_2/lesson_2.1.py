def hide_card(card_number:str):
    return f"{'*'*12}{card_number.replace(' ','')[-4:]}"

def same_parity(numbers:list):
    return [i for i in numbers if i%2==numbers[0]%2]

def is_valid(string:str):
    return True if string.isdigit() and 6>=len(string)>=4 and string.find(' ')==-1 else False

def print_given(*args, **kwargs):
    for i in args: print(i, type(i))
    for k,v in sorted(kwargs.items()): print(k,v, type(v))

def convert(string:str):
    if len([i for i in string if i.isupper()]) > len([i for i in string if i.islower()]): return string.upper()
    else: return string.lower()

def filter_anagrams(word:str, words:list):
    return [i for i in words if sorted(i)==sorted(word)]

def likes(names:list):
    if len(names)==0: return 'Никто не оценил данную запись'
    elif len(names)==1: return f'{names[0]} оценил(а) данную запись'
    elif len(names)==2: return f'{names[0]} и {names[1]} оценили данную запись'
    elif len(names)==3: return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else: return f'{names[0]}, {names[1]} и {len(names)-2} других оценили данную запись'

def index_of_nearest(numbers:list, number:int):
    if len(numbers)==0: return -1
    else:
        result=sorted([i for i in numbers], key=lambda x: abs(x-number))
        return numbers.index(result[0])

def spell(*args):
    result=dict()
    for i in args:
        if result.get(i.lower()[0], 0) < len(i): result[i.lower()[0]] = len(i)
    return result

def choose_plural(amount:int, declensions:tuple):
    if amount>=100: temp=amount%100
    else: temp=amount
    if temp==1: return f'{amount} {declensions[0]}'
    elif temp==2 or temp==3 or temp==4: return f'{amount} {declensions[1]}'
    elif 20>=temp>=5: return f'{amount} {declensions[2]}'
    elif 99>temp>20:
        if str(temp)[-1] == '1': return f'{amount} {declensions[0]}'
        elif str(temp)[-1] in '234': return f'{amount} {declensions[1]}'
        elif str(temp)[-1] in '567890': return f'{amount} {declensions[2]}'

"""Функция get_biggest() 🌶️🌶️ ПОЛНАЯ ЖОПА!!!!!!!!"""
def get_biggest(numbers:list):
    if len(numbers) != 0:
        len_number=max([len(str(i)) for i in numbers])
        result = sorted(numbers, key=lambda x: str(x)*len_number, reverse=True)
        itog=''
        for i in result: itog=itog+str(i)
        return int(itog)
    else: return -1

"""Тимур, Артур и новый курс"""
def timur_and_two_supermarkets(d_1:int, d_2:int, d_3:int):
    print([d_1+d_3+d_2, d_1+d_1+d_2+d_2, d_2+d_3+d_1, d_2+d_2+d_1+d_1, d_2+d_3+d_3+d_2, d_1+d_3+d_3+d_1])
# timur_and_two_supermarkets(int(input()), int(input()), int(input()))

def letter_in_string(text_1:str, text_2:str, text_3:str):
    result=[1 if i in 'AaBCcEeHKMOoPpTXxy' else 0 for i in text_1]
    result.extend([1 if i in 'AaBCcEeHKMOoPpTXxy' else 0 for i in text_2])
    result.extend([1 if i in 'AaBCcEeHKMOoPpTXxy' else 0 for i in text_3])
    if 1 in result and 0 in result: print('mix')
    elif 1 in result: print('en')
    else: print('ru')

def hernya_kakaya_to(my_list: list):
    result=list(range(1, my_list[0]+1))
    temp=result[my_list[1]-1:my_list[2]]
    result[my_list[1]-1:my_list[2]]=temp[::-1]
    temp=result[my_list[3]-1:my_list[4]]
    result[my_list[3]-1:my_list[4]]=temp[::-1]
    print(*result)

def bolee_odnogo(my_list:list):
    my_dict={i:my_list.count(i) for i in my_list}
    print(*sorted([k for k,v in my_dict.items() if v>=2]))

def maximalnaya_gruppa(n:int):
    my_dict = {i: [] for i in list(range(1, int(len(str(n)) * '9') + 1))}
    for i in list(range(1, n+1)):
        # summ=sum([int(j) for j in str(i)])
        summ=sum(list(map(int, str(i))))
        my_dict[summ].append(i)
    print(max([len(v) for k,v in my_dict.items()]))

def trudnosti_perevoda(n: int):
    result=input().split(', ')
    for i in range(n-1): result.extend(input().split(', '))
    my_dict={i:result.count(i) for i in result}
    print(*sorted([k for k,v in my_dict.items() if v==n]) if len([k for k,v in my_dict.items() if v==n])>=1 else ['Сериал снять не удастся'], sep=', ')

def shozie_slova(word:str, n: int):
    standart = [i for i in range(len(word)) if word[i] in 'ауоыиэяюёе']
    result=[]
    for i in range(n):
        temp_word=input()
        temp = [j for j in range(len(temp_word)) if temp_word[j] in 'ауоыиэяюёе']
        if temp==standart: result.append(temp_word)
    print(*result, sep='\n')





# def korporativnya_pochta(my_dict: dict, m: int):
#     result=[]
#     for i in range(m):
#         new_person_mail=input().replace('@beegeek.bzz', '')
#         if new_person_mail in my_dict.keys():
#             result.append(f'{new_person_mail}{my_dict.get(new_person_mail)+1}@beegeek.bzz')
#             my_dict[new_person_mail] = my_dict.get(new_person_mail)+1
#         else:
#             my_dict[new_person_mail]=0
#             result.append(f'{new_person_mail}@beegeek.bzz')
#     return result

# def current_mail_list_func():
#     "Формирование списка существующих почт"
#     current_mail_list=[input().replace('@beegeek.bzz', '') for i in range(int(input()))]
#     #Нахождение цифр в названии почты и формирование словаря
#     my_dict = dict()
#     for i in current_mail_list:
#         mail_name=''.join(' ' if element.isdigit() else element for element in i).strip()
#         number = ''.join(element if element.isdigit() else ' ' for element in i).strip()
#         if number=='': number=0
#         if mail_name not in my_dict: my_dict[mail_name]=[int(number)]
#         else: my_dict.get(mail_name).append(int(number))
#     return my_dict
#
# def korporativnya_pochta(my_dict: dict, m: int):
#     "Формирование списка почт новых пользователей"
#     result=[]
#     for i in range(m):
#         new_person_mail=input().replace('@beegeek.bzz', '')
#         number=0
#         if new_person_mail not in my_dict:
#             my_dict[new_person_mail]= [number]
#         else:
#             num_list=my_dict.get(new_person_mail)
#             while number in num_list: number+=1
#             my_dict[new_person_mail].append(number)
#         result.append(f'{new_person_mail}{number if number != 0 else ""}@beegeek.bzz')
#
#     print(*result, sep='\n')
#
# current_mail_list=current_mail_list_func()
# korporativnya_pochta(current_mail_list, int(input()))
#
# #КРАСИВОЕ РЕШЕНИЕ
# emails = set(input() for _ in range(int(input())))
# for _ in range(int(input())):
#     emp = input()
#     email = f'{emp}@beegeek.bzz'
#     count = 0
#     while email in emails:
#         count += 1
#         email = f'{emp}{count}@beegeek.bzz'
#     emails.add(email)
#     print(email)
#
# #КРАСИВОЕ РЕШЕНИЕ2
# digits, names = '0123456789', []
#
# for _ in range(int(input())):
#     name, _ = input().split('@')
#     names.append(name)
#
# for _ in range(int(input())):
#     name = input()
#     counter = 1
#     while name in names:
#         name = name.rstrip(digits) + str(counter)
#         counter += 1
#     names.append(name)
#     print(f'{name}@beegeek.bzz')

"""Файлы в файле 🌶️🌶️"""
def files_v_files():
    with open('files.txt', 'r', encoding='utf-8') as file:
        my_dict, n = dict(), len(file.readlines()) #Количенство строк в файле
        file.seek(0)
        for i in range(1,n+1):
            line=file.readline().split()
            file_name, file_type, file_size, file_size_type=line[0], line[0].split('.')[1], int(line[1]), line[2]

            #записываем в словарь по типам имена файлов списком и делаем списком размер файлов в байтах(!!!)
            if file_type not in my_dict:
                my_dict[file_type]=[file_name]
                if file_size_type =='B':
                    my_dict[f'Summary {file_type}:']=[file_size]
                elif file_size_type =='KB':
                    my_dict[f'Summary {file_type}:']=[file_size*1024]
                elif file_size_type=='MB':
                    my_dict[f'Summary {file_type}:'] = [file_size * 1024**2]
                elif file_size_type=='GB':
                    my_dict[f'Summary {file_type}:'] = [file_size * 1024**3]

            else:
                my_dict.get(file_type).append(file_name)
                if file_size_type =='B':
                    my_dict.get(f'Summary {file_type}:').append(file_size)
                elif file_size_type =='KB':
                    my_dict.get(f'Summary {file_type}:').append(file_size*1024)
                elif file_size_type=='MB':
                    my_dict.get(f'Summary {file_type}:').append(file_size*1024**2)
                elif file_size_type=='GB':
                    my_dict.get(f'Summary {file_type}:').append(file_size*1024**3)

        #изменяем суммарную размерность файлов в словаре
        for k,v in my_dict.items():
            if 'Summary' in k:
                if sum(my_dict[k]) > 1024**3: my_dict[k] = str(round(sum(my_dict[k])/1024**3)) + ' GB'
                elif 1024**3 > sum(my_dict[k]) > 1024**2: my_dict[k] = str(round(sum(my_dict[k]) / 1024**2)) + ' MB'
                elif 1024**2 > sum(my_dict[k]) > 1024: my_dict[k] = str(round(sum(my_dict[k]) / 1024)) + ' KB'
                else: my_dict[k] = str(my_dict.get(k)) + ' B'

        #вывод на печать требуемого
        for k, v in sorted(my_dict.items()):
            if 'Summary' not in k:
                print(*sorted(my_dict[k]), sep='\n')
                print('-'*10)
                print('Summary:', my_dict[f'Summary {k}:'])
                print()
files_v_files()

