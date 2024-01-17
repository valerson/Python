# print(sum(list(range(1, 11))))
import math
import time
# def calculate_it(func, *args)->tuple:
#     """
#     Функция возвращать кортеж, первым элементом которого является
#     возвращаемое значение функции func при вызове с аргументами *args,
#     а вторым — примерное время (в секундах), затраченное на вычисление этого значения.
#
#     :param func:
#     :param args:
#     :return:
#     """
#     start=time.monotonic()
#     result=func(*args)
#     end=time.monotonic()
#     return (result, end-start)
#
# def add(a, b, c):
#     time.sleep(3)
#     return a + b + c
#
# print(calculate_it(add, 1, 2, 3))

# import time
# def get_the_fastest_func(funcs, arg):
#     my_dict=dict()
#     for i in funcs:
#         start=time.monotonic()
#         i(arg)
#         end = time.monotonic()
#         my_dict[end-start]=i
#     result=sorted(my_dict)
#     # return result
#     return my_dict[result[0]]
#
# def slow(arg):
#     time.sleep(3)
# def fast(arg):
#     time.sleep(1)
# funcs = [slow, fast]
# print(get_the_fastest_func(funcs, 0))


# from math import factorial                   # функция из модуля math
# import time
# result=[]
# start=time.perf_counter()
# math.factorial(900)
# end=time.perf_counter()
# result.append(['math',end-start])
#
# def factorial_recurrent(n):                  # рекурсивная функция
#     if n == 0:
#         return 1
#     return n * factorial_recurrent(n - 1)
#
#
# def factorial_classic(n):                    # итеративная функция
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
# start=time.perf_counter()
# factorial_recurrent(900)
# end=time.perf_counter()
# result.append(['factorial_recurrent',end-start])
#
# start=time.perf_counter()
# factorial_classic(900)
# end=time.perf_counter()
# result.append(['factorial_classic',end-start])
#
# print(sorted(result, key=lambda x: x[1]))

# import time
# def for_and_append():  # с использованием цикла for и метода append()
#     iterations = 10_000_000
#     result = []
#     for i in range(iterations):
#         result.append(i + 1)
#     return result
#
# def list_comprehension():  # с использованием списочного выражения
#     iterations = 10_000_000
#     return [i + 1 for i in range(iterations)]
#
# result=[]
# for i in [for_and_append(), list_comprehension()]:
#     start=time.perf_counter()
#     x=i
#     end=time.perf_counter()
#     result.append((end-start)*10**4)
# print(result)

import time
def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result

def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]

def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)

result=[]
for i in [for_and_append(range(100_000)),list_function(range(100_000)),list_function(range(100_000))]:
    start=time.perf_counter()
    x=i
    end=time.perf_counter()
    result.append((end-start)*10**4)
print(result)