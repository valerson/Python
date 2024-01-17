# import csv
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.reader(file, delimiter=';', quotechar='"')
#     for index, row in enumerate(rows): # встроенную функцию enumerate() для нумерации строк.
#         if index > 5:
#             break
#         print(row)

# import csv
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';', quotechar='"')
#     for row in rows:
#         print(row)

# import csv
# with open('products.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';', quotechar='"')
#     expensive = sorted(rows, key=lambda item: int(item['price']), reverse=True)
#     for record in expensive[:5]:
#         print(record)

# import csv
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]
# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(columns)                 # запись заголовков
#     for row in data:                         # запись строк
#         writer.writerow(row)

# import csv
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]
# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(columns)
#     for row in data:
#         writer.writerow(row)

# import csv
# with open('grades.csv', 'r', encoding='utf-8') as file:
#     text=csv.reader(file, delimiter=';')
#     for i in text:
#         print(i)

# import csv
# with open('writing_test.csv', 'w', encoding='utf-8') as file:
#     fieldnames=['first_col','second_col']
#     writer=csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
#ИЛИ ТАК ЗАПИСАТЬ
      # writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
#     # записываем первую строку с названиями столбцов
#     writer.writeheader()
#     # записываем строку с данными
#     writer.writerow({'first_col': 'value1', 'second_col': 'value2'})

# import csv
# with open('writing_test.csv', 'w', encoding='utf-8') as file:
#     writer=csv.writer(file, delimiter=';')#, quoting=csv.QUOTE_MINIMAL)
#     # записываем строку с данными
#     writer.writerow(['first_col', 'second_col'])
#     # записываем строку с данными
#     writer.writerow(['value1', 'value2'])

# """Скидки"""
# import csv
# with open('C:\\Users\\79266\\Downloads\\sales.csv', 'r', encoding='utf-8') as file:
#     reader=csv.DictReader(file, delimiter=';')
#     print(*[i['name'] for i in reader if int(i['new_price']) < int(i['old_price'])], sep='\n')

# """Средняя зарплата"""
# import csv
# with open('C:\\Users\\79266\\Downloads\\salary_data.csv', 'r', encoding='utf-8') as file:
#     reader=csv.DictReader(file, delimiter=';')
#     my_dict=dict()
#
#     for i in reader:
#         if i['company_name'] not in my_dict: my_dict[i['company_name']]=[int(i['salary'])]
#         else: my_dict.get(i['company_name']).append(int(i['salary']))
#
#     file.seek(0)
#     company = set([i['company_name'] for i in reader if i['company_name']!='company_name'])
#     my_dict=sorted({i:sum(my_dict.get(i)) / len(my_dict.get(i)) for i in company}.items(), key=lambda x: x[1])
#     for k,v in my_dict:
#         print(k)


# """Сортировка по столбцу"""
# import csv
# with open('C:\\Users\\79266\\Downloads\\deniro.csv', 'r', encoding='utf-8') as file:
#     reader=csv.DictReader(file, fieldnames=[1,2,3], delimiter=',', quotechar='"')
#     n=int(input())
#     if n==1: reader=sorted(reader, key=lambda x: x[1])
#     else: reader=sorted(reader, key=lambda x: int(x[n]))
#     for i in reader:
#         print(i[1],i[2], i[3], sep=',')


# def csv_columns(filename:str)->dict:
#     import csv
#     with open(filename, 'r', encoding='utf-8') as file:
#         reader = csv.DictReader(file, delimiter=',')
#         my_dict={i:[] for i in reader.fieldnames}
#         for i in reader:
#             for j in my_dict: my_dict.get(j).append(i.get(j))
#         return my_dict
#
# csv_columns('exam.csv')

# """Популярные домены"""
# import csv
# with open('data.csv', 'r', encoding='utf-8') as file_in, open('domain_usage.csv', 'w', encoding='utf-8') as file_out:
#     reader=list(csv.reader(file_in, delimiter=','))[1:]
#     domain=[i[2].split("@")[1] for i in reader]
#
#     writer=csv.writer(file_out, delimiter=',', lineterminator='\n')
#     #Записали шапку
#     writer.writerow(['domain', 'count'])
#     result=[[i, domain.count(i)] for i in set(domain)]
#     #Записываем построчно в файл результат
#     for i in sorted(sorted(result), key=lambda x:x[1]):
#         writer.writerow(i)


# """Wi-Fi Москвы"""
# import csv
# with open('C:\\Users\\79266\\Downloads\\wifi.csv', 'r', encoding='utf-8') as file:
#     reader=list(csv.DictReader(file, delimiter=';'))
#     districts=dict.fromkeys(list(set([i['district'] for i in reader])),0)
#
#     for i in districts:
#         for j in reader:
#             if j['district'] in i:
#                 districts[i]=districts.get(i)+int(j['number_of_access_points'])
#
#     districts = sorted(districts.items(), key=lambda x: x[0].replace('район', '').strip())
#
#     for i in sorted(districts, key=lambda x:x[1], reverse=True):
#         print(f'{i[0]}: {i[1]}')

# """Последний день на Титанике"""
# import csv
# with open('C:\\Users\\79266\\Downloads\\titanic.csv', 'r', encoding='utf-8') as file:
#     reader = list(csv.DictReader(file, delimiter=';'))
#     result=[i for i in reader if i['survived']=='1' and float(i['age'])<18]
#     for i in sorted(result, key=lambda x: x['sex'], reverse=True):
#         print(i['name'])

# """Лог-файл"""
# import csv
# from datetime import datetime
# with open('C:\\Users\\79266\\Downloads\\name_log.csv', 'r', encoding='utf-8') as file_in, open('C:\\Users\\79266\\Downloads\\new_name_log.csv', 'w', encoding='utf-8') as file_out:
#     #прочитали все из файла в список словарей
#     reader=list(csv.DictReader(file_in, delimiter=','))
#     #применили формат даты к дате
#     for i in reader: i['dtime'] = datetime.strptime(i['dtime'], '%d/%m/%Y %H:%M')
#     #отсортировали список словарей по дате от старой к новой
#     reader=sorted(reader, key=lambda x: x['dtime'])
#     #сформировали словарь с актуальными данными по адресу почты
#     my_dict={i['email']:i for i in reader}
#     # отсортировали словарь по адресу почты
#     my_dict=[v for k, v in my_dict.items()]
#     my_dict=sorted(my_dict, key=lambda x:x['email'])
#
#     # применили обратно формат даты к дате
#     for i in my_dict: i['dtime'] = datetime.strftime(i['dtime'], '%d/%m/%Y %H:%M')
#
#     #запись в файл в требуемом формате
#     fieldname = ['username', 'email', 'dtime']
#     writer=csv.DictWriter(file_out, delimiter=',', fieldnames=fieldname, lineterminator='\n')
#     #Записали заголовок
#     writer.writeheader()
#     #Записали каждую строку
#     for i in my_dict:
#         writer.writerow(i)

"""Проще, чем кажется 🌶️"""
import csv
def condense_csv(filename:str, id_name:str):
    with open(filename, 'r', encoding='utf-8') as file, open('condensed.csv', 'w', encoding='utf-8') as file_out:
        reader=list(csv.DictReader(file,delimiter=',',fieldnames=[id_name,'characteristic', 'value']))

        #сформировали словарь по каждому объекту с всеми свойствами и значениями
        my_dict=dict()
        for i in reader:
            if i[id_name] not in my_dict:
                my_dict[i[id_name]]={i['characteristic']:i['value']}
            else:
                temp={i['characteristic']:i['value']}
                my_dict.get(i[id_name]).update(temp)
        # print(my_dict)

        # Сформировали список строк для записи в файл
        result=[]
        for k,v in my_dict.items():
            temp=[k]
            for k_2,v_2 in v.items():
                temp.append(v_2)
            result.append(temp)
        # print(result)

        #Сформировали шапку файла
        fieldname = [id_name, *[k for k,v in my_dict.get(reader[0][id_name]).items()]]
        #запись в файл в требуемом формате
        writer=csv.DictWriter(file_out, delimiter=',', fieldnames=fieldname, lineterminator='\n')
        #Записали заголовок
        writer.writeheader()
        #Записали каждую строку
        for i in result:
            zipped=list(zip(fieldname,i))
            writer.writerow(dict(zipped))

# condense_csv('data.csv', id_name='ID')

# """Возрастание классов 🌶️"""
# import csv
# #читаем
# with open('C:\\Users\\79266\\Downloads\\student_counts.csv', 'r', encoding='utf-8') as file_input, open('C:\\Users\\79266\\Downloads\\sorted_student_counts.csv', 'w', encoding='utf-8') as file_output:
#     reader = csv.DictReader(file_input, delimiter=',')
#
#     #изменили ключи в словаре добавив в номера классов 0 и 00 в год для корреткной сортировки
#     new_fieldnames=list(map(lambda x: x.rjust(4,'0'), reader.fieldnames))
#     new_fieldnames[0]='00year'
#     #создали новую шапку с названием классов и года без лишних нудей
#     new_fieldnames_2=sorted(new_fieldnames)
#     new_fieldnames_2[0] = 'year'
#     new_fieldnames_2 = list(map(lambda x: x.lstrip('0'), new_fieldnames_2))
#
# #записываем
#     writer=csv.DictWriter(file_output, fieldnames=new_fieldnames_2, delimiter=',', lineterminator='\n')
#     writer.writeheader()
#     for i in reader:
#         writer.writerow(i)

# """Возрастание классов 🌶️"""
# import csv
# #читаем
# with open('C:\\Users\\79266\\Downloads\\student_counts.csv', 'r', encoding='utf-8') as file_input:
#     reader = csv.DictReader(file_input, delimiter=',')
#
#     #изменили ключи в словаре добавив в номера классов 0 и 00 в год для корреткной сортировки
#     reader.fieldnames=list(map(lambda x: x.rjust(4,'0'), reader.fieldnames))
#     reader.fieldnames[0]='00year'
#     #создали новую шапку с названием классов и года без лишних нудей
#     new_fieldnames=sorted(reader.fieldnames)
#     new_fieldnames[0] = 'year'
#     new_fieldnames = list(map(lambda x: x.lstrip('0'), new_fieldnames))
#
#     #создаем список из значений (только год, и количенство учеников в классах по порядку) отсортированного словаря
#     result_list=[[v for k,v in sorted(i.items())] for i in reader]
#
# #записываем
# with open('C:\\Users\\79266\\Downloads\\sorted_student_counts.csv', 'w', encoding='utf-8') as file_output:
#     writer=csv.DictWriter(file_output, fieldnames=new_fieldnames, delimiter=',', lineterminator='\n')
#     writer.writeheader()
#
#     for i in result_list:
#         zipped=list(zip(new_fieldnames,i))
#         writer.writerow(dict(zipped))


# #КРАСИВОЕ РЕШЕНИЕ
# import csv
#
# with open('C:\\Users\\79266\\Downloads\\student_counts.csv', encoding='utf-8') as file, open('C:\\Users\\79266\\Downloads\\sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as f:
#     reader = csv.DictReader(file)
#     my_list = reader.fieldnames
#     sorted_list = sorted(my_list, key=lambda x: (0, "") if x == "year" else (int(x.split('-')[0]), x.split('-')[1]))
#
#     writer = csv.DictWriter(f, fieldnames=sorted_list)
#     writer.writeheader()
#     for row in reader:
#         writer.writerow(row)

# """Голодный студент 🌶️"""
# import csv
# with open('C:\\Users\\79266\\Downloads\\prices.csv', encoding='utf-8') as file:
#     reader=csv.DictReader(file, delimiter=';')
#     result=[]
#     for i in reader:
#         market_name=i.pop('Магазин')
#         product_price, product_name = [(int(v),k) for k,v in sorted(i.items(), key=lambda x: int(x[1]))]  [0]
#         result.append([product_price, product_name, market_name])
#
#     temp = min(result, key=lambda x: (x[0], x[1], x[2]))
#     print(f'{temp[1]}: {temp[2]}')

    # result=sorted(result, key=lambda x: x[2])
    # result = sorted(result, key=lambda x: x[1])
    # result = sorted(result, key=lambda x: x[0])
    # print(f'{result[0][1]}: {result[0][2]}')




































