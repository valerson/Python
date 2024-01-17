# import sys
# for line in sys.stdin:
#     print(line.strip('\n'))
#
# data = [line.strip() for line in sys.stdin]

# import sys
#
# print('Hello')
# sys.stdout.write('world!')
# print('from')
# sys.stdout.write('python\n')
# print('Bye-bye')

# import sys
#
# temp = sys.stdout
# sys.stdout = open('log.txt', 'w')
# print('testing123')
# print('another line')
# sys.stdout.close()
# sys.stdout = temp
# print('back to normal')


# import sys
# for i in sys.stdin:
#     print(i[::-1].strip('\n'))

# import sys
# """Программа должна вывести единственное число — количество дней
# между максимальной и минимальной датами введенной последовательности"""
# from _datetime import datetime, timedelta
# maximum=datetime.strptime(input(), '%Y-%m-%d')
# minimum=maximum
# for i in sys.stdin:
#     temp = datetime.strptime(i.strip('\n'), '%Y-%m-%d')
#     if temp>maximum: maximum=temp
#     elif temp<minimum: minimum=temp
# print((maximum-minimum).days)

# #ХОРОШЕЕ РЕШЕНИЕ
# import sys
# from datetime import datetime
# date = [datetime.fromisoformat(i.strip()) for i in sys.stdin]
# print((max(date) - min(date)).days)


# import sys
# anri, dima=[], []
# for i in sys.stdin:
#     if len(anri)==len(dima):
#         anri.append(int(i))
#         winner = ['Анри' if int(i)%2==0 else 'Дима']
#     else:
#         dima.append(int(i))
#         winner = ['Дима' if int(i) % 2 == 0 else 'Анри']
# print(*winner)
#
# #КРАСИВОЕ РЕШЕНИЕ
# import sys
# pl1, pl2 = 'Дима', 'Анри'
# for num in sys.stdin:
#     pl1, pl2 = pl2, pl1
# print(pl1 if int(num) % 2 == 0 else pl2)

# import sys
# my_list=[int(i) for i in sys.stdin]
# if len(my_list)==0: print("Нет учеников")
# else:
#     print(f'Рост самого низкого ученика: {min(my_list)}')
#     print(f'Рост самого высокого ученика: {max(my_list)}')
#     print(f'Средний рост: {sum(my_list)/len(my_list)}')

# import sys
# count=[1 for i in sys.stdin if i.strip()[0]=='#']
# print(sum(count))

# import sys
# for i in sys.stdin:
#     if i.strip(' ')[0]!='#':
#         print(i.strip('\n'))

# import sys
# my_list=[]
# for i in sys.stdin:
#     if '/' in i.strip('\n'): my_list.append(i.strip('\n').split(' / '))
#     else: trigger=i.strip()
#
# for i in sorted(sorted(my_list), key=lambda x: x[2]):
#     if i[1].strip() in trigger: print(i[0])

# import sys
# from datetime import datetime
# list_date=[datetime.strptime(i.strip('\n'),'%d.%m.%Y') for i in sys.stdin]
# if list_date==sorted(list_date) and len(list_date)==len(set(list_date)): print("ASC")
# elif list_date==sorted(list_date, reverse=True) and len(list_date)==len(set(list_date)): print("DESC")
# else: print("MIX")

# import sys
# my_list=[int(i) for i in sys.stdin]
# shag_1, shag_2=my_list[1]-my_list[0], my_list[1]/my_list[0]
# ariph_grogress, geometry_progress=[], []
# for i in range(1, len(my_list)):
#     if my_list[i]==my_list[i-1]+shag_1: ariph_grogress.append(1)
#     if my_list[i]==my_list[i-1]*shag_2: geometry_progress.append(1)
# if len(ariph_grogress)==len(my_list)-1: print('Арифметическая прогрессия')
# elif len(geometry_progress)==len(my_list)-1: print('Геометрическая прогрессия')
# else: print('Не прогрессия')



