# try:
#     # контролируемый код
# except тип_ошибки_1:
#     # код обработки ошибки (исключения)
# except тип_ошибки_2:
#     # код обработки ошибки (исключения)
# ...
# except тип_ошибки_n:
#     # код обработки ошибки (исключения)

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print('Частное чисел равно', num1 / num2)
# except (ValueError, IndexError, KeyError):
#     print('Тут обрабатываются сразу три типа ошибок!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except:
#     print('Если не сработал ни один из предыдущих блоков except.')
#
# print('Работа программы завершена!')

# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
#               {'Likes': 13, 'Comments': 2, 'Shares': 1},
#               {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
#               {'Comments': 4, 'Shares': 2},
#               {'Photos': 8, 'Comments': 1, 'Shares': 1},
#               {'Photos': 3, 'Likes': 19, 'Comments': 3}]
# total_likes = 0
# for post in blog_posts:
#
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#         # print('нет ключа!!')
#         total_likes -= 1
# print(total_likes)

"""Only numbers"""
import sys
my_list, count, summ=[i for i in sys.stdin], 0, 0.0
for elem in my_list:
    try:
        summ+=float(elem)
    except ValueError:
        count+=1
print(int(summ) if summ.is_integer() else summ)
print(count)








