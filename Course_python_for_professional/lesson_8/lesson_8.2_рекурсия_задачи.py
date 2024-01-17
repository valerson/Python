# def draw_rect(width, height, step):
#     if step < height:
#         print('*' * width)
#         draw_rect(width, height, step + 1)
# draw_rect(4, 3, 0)

# def draw_rect(width, height):
#     def rec(step):
#         if step < height:
#             print('*' * width)
#             rec(step + 1)
#     rec(0)

# def draw_rect(width, height):
#     if height>0:
#         print('*'*width)
#         height-=1
#         draw_rect(width, height)
# draw_rect(4,4)


# def print_numbers(start, end):
#     def rec(num):
#         if num <= end:
#             print(num)
#             rec(num + 1)
#     rec(start)

# def print_numbers(start, end):
#     if start<=end:
#         print(start)
#         start+=1
#         print_numbers(start, end)
# print_numbers(0,7)

# """Подозрительно просто 🤫"""
# def traffic(number):
#     if number>0:
#         print('Не парковаться')
#         number-=1
#         traffic(number)
# traffic(3)

# """Подозрительно просто 🤐"""
# def numbers(start=1, end=100):
#     if start<=end:
#         print(start)
#         start+=1
#         numbers(start,end)
# numbers()

# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341,
#            437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331,
#            323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127,
#            984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777,
#            805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341,
#            437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331,
#            323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127,
#            984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777,
#            805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
# def num_print(numbers):
#     def elem(element=0):
#         if element<len(numbers):
#             print(f'Элемент {element}: {numbers[element]}')
#             elem(element+1)
#     elem()
# num_print(numbers)

# """Обратный порядок"""
# def reverse_sequence(number=9999):
#     if number!=0:
#         number = int(input())
#         reverse_sequence(number)
#         print(number)
# reverse_sequence()

# """Обратный порядок - РАСИВАЯ ВЕРСИЯ"""
# def reverse_sequence():
#     number = int(input())
#     if number!=0:
#         reverse_sequence()
#     print(number)
# reverse_sequence()

# """Функция triangle() 😥"""
# def triangle(h:int):
#     if h>0:
#         print('*'*h)
#         triangle(h-1)
# triangle(3)

# """Функция triangle() 😰"""
# def triangle(h:int):
#     def do_it(count=1):
#         if count<=h:
#             print('*'*count)
#             do_it(count+1)
#     do_it()
#КРАСИВОЕ РЕШЕНИЕ
# def triangle(h:int):
#     if h>0:
#         triangle(h-1)
#         print('*'*h)

# """Песочные часы"""
# def hourglass(num=16,ind=1):
#     if ind<=3:
#         print(str(str(ind)*num).center(16))
#         hourglass(num-4,ind+1)
#         print(str(str(ind)*num).center(16))
#     elif ind==4:
#         print(str(str(ind)*num).center(16))
#
# hourglass()

# """Песочные часы2"""
# def hourglass(num=16,ind=1):
#     if ind<4:
#         print('ind=',ind)
#         # print(str(str(ind)*num).center(16))
#         hourglass(num-4,ind+1)
#     # print(str(str(ind)*num).center(16))
#     print('ind=', ind)
#
# hourglass()

"""Функция print_digits() 😉"""
# def print_digits(number):
#     def do_it(count=1):
#         if (len(str(number))-count)>=0:
#             print(str(number)[len(str(number))-count])
#             do_it(count+1)
#     do_it()

# def print_digits(number):
#     print(number%10)
#     if number>10:
#         print_digits(number//10)
#
# print_digits(12345)

# """Функция print_digits() 😎"""
# def print_digits(numbers):
#     print(str(numbers)[:1])
#     if numbers:
#         numbers=str(numbers)[1:]
#         print_digits(numbers)

# print_digits(12345)
