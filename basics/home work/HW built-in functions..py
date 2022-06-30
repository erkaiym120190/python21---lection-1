
# Task 1

# import functools
# list_ = [1, 2, 3, 4]  
# result = functools.reduce(lambda a, b: a + b, list_)
# print(result)


# Task 2

# list_ = [1, 5, -9, 6, -4] 
# result = all(i > 3 for i in list_)
# print(result)


# Task 3

# list_ = [5, 8, 4, 6, 7]
# result = any(i < 0 for i in list_)
# print(result)


# Task 4

# list_ = [1, 2, 3, 4] 
# result = list(map(lambda x: x ** 2, list_))
# print(result)


# Task 5

# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda a: a%2 == 0, list_))
# print(result)


# Task 6

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda i: len(i) > 7, list_))
# print(result)


# Task 7

# from functools import reduce
# list_ = [5, 6, 7, 8] 

# def mul(a, b):
#     return a * b

# result = reduce(mul, list_)
# print(result)


# Task 8

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 

# list2 = list(filter(lambda a: a%2 == 0, list_))
# list3 = list(filter(lambda a: a%2 != 0, list_))

# result = (f'even: {len(list2)}, odd: {len(list3)}')
# print(result)


# Task 9

# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda a: a > 0, list_))
# print(result)


# Task 10

# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)


# CLASS WORK TASK 1

# Создайте список, который будет содержать различные типы данных. 
# Напишите программу, которая будет находить корень чисел, 
# содержащихся в созданном списке. Используйте встроенные функции.

# from math import sqrt
# list_ = [25, 'string', 625, True, ''name'', 'error', 144, 169, 'winter', 123]
# new_list = list(map(lambda a: round(sqrt(a)), filter(lambda a: type(a) == int, list_)))
# print(new_list)


# CLASS WORK TASK 2

# 2) Реализуйте следующую программу: есть студенты, которые сдали экзамен. 
# Вам необходимо сохранить имена и баллы тех студентов, которые не прошли проходной балл (<60). 
# Далее каждому студенту вам необходимо отправить письмо, которое говорит о том, 
# что этого студента собираются отчислить.

# students = [{'name': 'Aydin', 'balls': 124}, 
#             {'name': 'Bermet', 'balls': 56}, 
#             {'name': 'Kanatbek', 'balls': 120}, 
#             {'name': 'Aijan', 'balls': 59}]
# list_ = list(filter(lambda a: a['balls'] < 60, students))
# names = list(map(lambda a: a['name'], list_))
# balls = list(map(lambda a: a['balls'], list_))
# list1 = list(zip(names, balls))
# list2 = list(map(lambda a: f'{a[0]}, Вы будете отчислены, в связи с недостаточным количеством набранных баллов.', list1))
# print(list2)


# CLASS WORK TASK 3

# Создайте список с буквами. Напишите программу, которая склеит все буквы в списке в строку. 
# Не использовать метод join() и циклы.

# import functools
# list_ = ['m', 'e', 'g', 'a', 'l', 'a', 'd', 'o', 'n']
# list2 = functools.reduce(lambda a, b: a + b, list_)
# print(list2)










