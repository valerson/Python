# beegeek = lambda: 'beegeek'
# print(beegeek())

total = 0
with open('exam.txt', 'r', encoding='utf-8') as file:
    for _ in file.readlines():
        total = total + 1
# print(total)


def get_max_index(numbers):
    max_index = 0
    max_value = numbers[0]

    for index, value in enumerate(numbers, 0):
        if value > max_value:
            max_index = index
            max_value = value

    return max_index

print(get_max_index([1,2,3,4,5,6,7,2]))











