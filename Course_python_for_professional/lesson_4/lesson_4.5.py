# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     zip_file.printdir()


# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time)                # дата изменения файла


# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     print(*info, sep='\n')


# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()                # получаем названия всех файлов архива
#     last_file = zip_file.getinfo(info[-4])    # получаем информацию об отдельном файле
#     print(last_file.file_size)
#     print(last_file.compress_size)
#     print(last_file.filename)
#     print(last_file.date_time)


# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read())


# from zipfile import ZipFile
# with ZipFile('archive.zip', mode='w') as zip_file:
#     zip_file.write('program.py')
#     zip_file.write('lse.jpeg')
#     print(zip_file.namelist())


# from zipfile import ZipFile
# with ZipFile('archive.zip', mode='w') as zip_file:
#     zip_file.write('program.py', 'new_program.py')  # первый аргумент - это имя файла
#     zip_file.write('lse.jpeg', 'lse1.jpeg')         # второй аргумент - это имя файла в архиве
#     print(zip_file.namelist())


# from zipfile import ZipFile
# with ZipFile('test.zip', mode='a') as zip_file:
#     zip_file.write('program.py', 'test/program.py')
#     zip_file.write('lse.jpeg')
#     print(*zip_file.namelist(), sep='\n')


# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     zip_file.extract('test/Картинки/avatar.png')
#     zip_file.extract('test/Программы/image_util.py')
#     zip_file.extract('lse.jpeg')


# from zipfile import ZipFile
# with ZipFile('test.zip') as zip_file:
#     zip_file.extractall()


# from zipfile import ZipFile
# with ZipFile('workbook.zip') as file_zip:
#     print(sum([1 for i in file_zip.namelist() if '.' in i]))


# from zipfile import ZipFile
# with ZipFile('C:\\Users\\79266\\Downloads\\workbook.zip') as zip_file:
#     text=zip_file.infolist()
#     file_size=sum([i.file_size for i in text])
#     zip_file_size=sum([i.compress_size for i in text])
#     print(f'Объем исходных файлов: {file_size} байт(а)\nОбъем сжатых файлов: {zip_file_size} байт(а)')

# """Наилучший показатель"""
# from zipfile import ZipFile
# with ZipFile('C:\\Users\\79266\\Downloads\\workbook.zip') as zip_file:
#     temp=zip_file.infolist()
#     result=[[i.filename, i.compress_size/i.file_size] for i in temp if i.file_size!=0]
#     print(sorted(result, key=lambda x: x[1])[0][0].split('/')[1])

# """Избранные"""
# from zipfile import ZipFile
# import sys
# with ZipFile('C:\\Users\\79266\\Downloads\\workbook.zip') as zip_file:
#     data=zip_file.infolist()
#     result=[i.filename.split('/')[1] if '/' in i.filename else i.filename for i in data if i.date_time > (2021, 11, 30, 14, 22, 00) and i.file_size>0]
#     print(*sorted(result), sep='\n')

# """Форматированный вывод"""
# from zipfile import ZipFile
# from datetime import datetime
# with ZipFile('C:\\Users\\79266\\Downloads\\workbook.zip') as zip_file:
#     data=zip_file.infolist()
#     for i in sorted(data, key=lambda x: x.filename.split('/')[-1]):
#         if i.filename.split('/')[-1]!='':
#             print(i.filename.split('/')[-1])
#             print(f'  Дата модификации файла: {datetime(*i.date_time)}')
#             print(f'  Объем исходного файла: {i.file_size} байт(а)')
#             print(f'  Объем сжатого файла: {i.compress_size} байт(а)')
#             print('')


# from zipfile import ZipFile
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
# with ZipFile('files.zip', mode='w') as zip_file:
#     for i in file_names:
#         zip_file.write(i)


# from zipfile import ZipFile
# import os.path
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
# with ZipFile('files.zip', mode='w') as zip_file:
#     name_file_small_size=[i for i in file_names if int(os.path.getsize(i))<=100]
#     [zip_file.write(i) for i in name_file_small_size]


# from zipfile import ZipFile
# def extract_this(zip_name:str, *args):
#     with ZipFile(zip_name, mode='r') as zip:
#         if args:
#             for i in args:
#                 zip.extract(i)
#         else:
#             zip.extractall()
#         [zip.extract(i.filename) for j in args for i in zip.infolist() if j in i.filename]

# """Шахматы были лучше 🌶️"""
# from zipfile import ZipFile
# import json
#
# def is_json_correct(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file_json:
#         try:
#             json.load(file_json)
#             return True
#         except: #json.decoder.JSONDecodeError:
#             return False
#
# def processing_file(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file_json:
#         data=json.load(file_json)
#         return [data['first_name'], data['last_name'], data['team']]
#
#
# with ZipFile('C:\\Users\\79266\\Downloads\\data.zip', mode='r') as zip:
#     result=[]
#     for i in zip.infolist():
#         if '.json' in i.filename:
#             zip.extract(i.filename)
#             if is_json_correct(i.filename):
#                 #исполнение программы
#                 temp=processing_file(i.filename)
#                 if temp[2]=='Arsenal': result.append(temp[:2])
#
#     for i in sorted(result, key=lambda x: x[0]):
#         print(*i)

def dictonary_do(my_list:list)->dict:
    """
    Функция делает словарь из списка по типу [1,2,3,4] {1:{2:{3:4}}}
    :param my_list:list
    :return:dict
    """
    if len(my_list)==2:
        return [str(my_list[0]+' '+ my_list[1])]
    else:
        return {my_list[0]:dictonary_do(my_list[1:])}


"""Структура архива 🌶️🌶️"""
from zipfile import ZipFile
def dimensionality_file(number:int)->str:
    """
    функция переводит количество байтов в КБ, МБ, ГБ и выводит и число и размерность
    :param number:
    :return:
    """
    if 0<number<=1024: return f'{number} B'
    elif 1024<=number<1024**2: return f'{round(number/1024)} KB'
    elif 1024**2 <= number < 1024 ** 3: return f'{round(number / (1024**2))} MB'
    elif 1024**3 <= number: return f'{round(number / (1024**3))} GB'

with ZipFile('C:\\Users\\79266\\Downloads\\test.zip', mode='r') as zip:
    my_list=[]
    delete={}
    for i in zip.infolist():
        temp=[str(i.filename).replace('/','') + ' ' + dimensionality_file(int(i.file_size)) if int(i.file_size)!=0 else str(i.filename).replace('/','')]
        if len(delete)>0:
            for j in delete:
                temp[0] = temp[0].replace(j.strip(), delete.get(j))
        print(temp[0])

        if int(i.file_size) == 0:
            delete[temp[0]]='  '
















