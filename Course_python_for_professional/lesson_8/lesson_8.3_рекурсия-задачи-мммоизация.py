# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(4))


# def sum_to(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum_to(n-1)
# print(sum_to(5))


# def recursion_sum(nums:list):
#     if len(nums)==1:
#         return nums[0]
#     else:
#         return nums.pop()+recursion_sum(nums)
# print(recursion_sum([1,2,3,4]))


# def fibonacci(n):
#     if n<=2:
#         return 1
#     else:
#         return fibonacci(n-2)+fibonacci(n-1)
# print(fibonacci(6))

# #мемоизация (кеширование)
# cache={1:1, 2:1} # ключ - номер числа, значение - число Фибоначчи
# def fibonacci(n):
#     result=cache.get(n,0)
#     if result==0:
#         result=fibonacci(n-2)+fibonacci(n-1)
#         cache[n]=result
#     return result

# #убрали глобальную переменную cache
# def fib(n):
#     cache = {1: 1, 2: 1}
#     def fib_rec(n):
#         result = cache.get(n)
#         if result is None:
#             result = fib_rec(n - 2) + fib_rec(n - 1)
#             cache[n] = result
#         return result
#     return fib_rec(n)


# """Количество цифр"""
# def count_number(number:int):
#     if number<10:
#         return 1
#     else:
#         return 1+count_number(number//10)
#
# print(count_number(int(input())))

# """Сумма цифр"""
# def sum_numbers(number:int):
#     if number<10:
#         return number
#     else:
#         return number%10+sum_numbers(number // 10)
# print(sum_numbers(int(input())))


# """Функция number_of_frogs()"""
# def number_of_frogs(year:int):
#     if year==1:
#         return 77
#     else:
#         return 3*(number_of_frogs(year-1)-30)
#
# print(number_of_frogs(2))

# """Функция range_sum()"""
# def range_sum(numbers,start,end):
#     if numbers[start]==numbers[end]:
#         return numbers[end]
#     else:
#         return numbers[start]+range_sum(numbers,start+1,end)
#
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))

# """Обычное возведение в степень"""
# def get_pow(a:int,n:int):
#     if n==0:
#         return 1
#     else:
#         return a*get_pow(a,n-1)
#
# print(get_pow(99, 0))

"""Быстрое возведение в степень"""
def get_fast_pow(a: int, n: int):
    if n == 0:
        return 1
    elif n==1:
        return a
    elif n==2:
        return a*a
    elif n % 2 != 0:
        return a * get_fast_pow(a, n - 1)
    else:
        return get_fast_pow(a*a, n / 2)
    pass

"""Функция recursive_sum()"""
def recursive_sum(a:int,b:int):
    def func(a, b, count=0):
        if count == a:
            return b
        else:
            return 1 + func(a, b, count + 1)
    return func(a,b)
# print(recursive_sum(5,6))

#ПРОСТОЕ И КРАСИВОЕ РЕШЕНИЕ
def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1)

# #РАЗНИЦА МЕЖДУ a и b
# def func(a, count=0):
#     if count==a:
#         return 0
#     else:
#         return 1+func(a, count+1)

"""Функция is_power()"""
def is_power(number):
    if number==1 or number/2==1:
        return True
    elif number%2==0:
        return is_power(number/2)
    else:
        return False


"""Функция tribonacci()"""
memo={1:1,2:1,3:1}
def tribonacci(n):
    if n==1 or n==2 or n==3:
        return 1
    elif memo.get(n):
        result=memo.get(n)
    else:
        result=tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
        memo[n]=result
    return result

"""Функция is_palindrome()"""
def is_palindrome(string):
    if len(string)==0 or len(string)==1:
        return True
    elif string[0]==string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

"""Функция to_binary()"""
def to_binary(number):
    def func(number):
        if number==0:
            return '0'
        elif number==1:
            return '1'
        elif number%2==0:
            return '0'+ func(number//2)
        elif number%2!=0:
            return '1' + func(number//2)
    return func(number)[::-1]

"""Без циклов"""
def mat(number):

    def minus(n):
        if n<=0:
            return n
        else:
            print(n)
            return minus(n-5)

    def plus(n):
        if n==number:
            print(n)
            return n
        else:
            print(n)
            return plus(n+5)

    plus(minus(number))
mat(int(input()))

#ОЧЕКЕЬ КРАСИВОЕ И ПРОСТОЕ РЕШЕНИЕ
def foo(n):
    if n <= 0:
        print(n)
    else:
        print(n)
        foo(n - 5)
        print(n)

foo(int(input()))

