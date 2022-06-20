# Classroom 1

# 1 variant
# list_users = ['Aydin', 'Gulya', 'Kanat', 'Mirlan', 'Erke', 'Urmat'] 
# vowels = ['a', 'e', 'o', 'i', 'u', 'y']
# list_users2 = [i for i in list_users if  i[0].lower() in vowels]
# print(list_users2)

# 2 variant
# list_users = ['Aydin', 'Gulya', 'Kanat', 'Mirlan', 'Erke', 'Urmat'] 
# list_users2 = [i for i in list_users if  i[0] == 'A' or i[0] == 'E' or i[0] == 'O' or i[0] == 'I' or i[0] == 'U' or i[0] == 'Y']
# print(list_users2)

# Classroom 2

# a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
# a1 = {key: {key1: value1 + 2 for key1, value1 in value.items()} for key, value in a.items()}
# print(a1)

# Classroom 3

# list_ = list(range(1,11))
# set_ = {i**2  if i%2 == 0 else i*3 for i in list_}
# print(set_)

# Classroom 4

# string = input()
# vowels = ['a', 'e', 'o', 'i', 'u', 'y']
# list_ = [i for i in string if i.lower() in vowels]
# print(len(list_))


# Task 1

# list_ = [i for i in range(1,101)]
# print(list_)

# Task 2

# list_ = [i for i in range(1,51) if i % 2 != 0]
# print(list_)

# Task 3

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i % 2 == 0 and i > 0]
# print(int_list)

# Task 4

# list_ = [i**2 for i in range(1,26)]
# print(list_)

# Task 5

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(i) for i in str_list]
# print(int_list)

# Task 6

# list_ = [i**2 if i%2 == 0 else i for i in range(1,11)]
# print(list_)

# Task 7

# list_ = [True if i%2 == 0 else False for i in range(1,11)]
# print(list_)

# Task 8

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['shorter' if len(i) <= 4 else 'longer' for i in list_name]
# print(new_list)

# Task 9

# dict_ = {i: i**2 for i in range(1,11)}
# print(dict_)

# Task 10

# Запросите у пользователя число от 1 до 10 в переменную n. Затем пройдитесь по промежутку чисел от 1 до 500(включительно) 
# и запишите в словарь dict_, только те числа, которые кратны числу n (делятся на число n без остатка), 
# введенное пользователем. Ключом будет само число, а значением его квадрат.

# n = int(input())
# dict_ = {i: i**2 for i in range(1,501) if i % n == 0}
# print(dict_)

# Task 11

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: [i for i in range(1,v+1)] for k, v in a.items()}
# print(dict_)

# Task 12

# Создайте словарь dict_ где ключами будут строки, а значениями произвольные числа. 
# Затем пройдитесь по элементам и запишите в a вместо значения строку 'even', если значение четное, 
# а если нет то 'odd'.

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k: 'even' if v%2 == 0 else 'odd' for k, v in dict_.items()}
# print(a)

# Task 13

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list1 = string_.split()
# list_ = [num for num in list1 if num.isdigit()]
# print(list_)

# Task 14

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict = {key: in_k 
#             for key, value in dict_.items() 
#             for in_k, in_v in value.items() 
#             # if list(value.keys()).index(in_k) == list(value.values()).index(max(list(value.values())))}
#             if in_v == max(value.values())}
# print(new_dict)

# Task 15

# Дан словарь my_dict значениями в котором являются другие словари.
# Создайте новый словарь dict_, оставив те же ключи, но заменив значения, 
# значениями внутренних словарей.

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {key: inner_value for key, value in my_dict.items() for inner_value in value.values()}
# print(dict_)

# Task 16 (Экстра задание #1)

# Создайте список list_ от 0 до 10 включительно c помощью специальной функции которая генерирует последовательно чисел,
# отфильтруйте список оставив в нем только четные элементы,
# затем разделите каждый элемент на 2 и выведите результат,
# нужно работать только с одним списком, нельзя создавать доп. списки.
# Необходимо использовать list comprehension
# Распечатайте результат.

# list_ = [i/2 for i in range(0,11) if i%2 == 0]
# print(list_)

# Task 17 (Экстра задание #2)

# Создайте словарь dict_ в котором ключами будут числа, а значениями строки. Перебирите словарь циклом:
# если ключ четный, нужно заменить его значение на длину этого значения
# если ключ нечетный то возвести длинну его значения в 3 степень
# Распечатайте dict_.
# Нужно работать только с одним словарем, нельзя создавать доп. словарь. Необходимо использовать dict comprehension.


# dict_ = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six'}
# print({key : len(val) ** 3 if key % 2 else len(val) for key, val in dict_.items()})

# Task 18 (Экстра задание #3)???????????????????????????????????????????????????????????????????????????????

# Создайте 2 сета set1 и set2 из 10 рандомных элементов
# Затем объедините их (специальным методом) в перменную full_set,
# И если их длина меньше 20, то вы должны вывести сообщение:
# "В этом сете было 3 повторения, его длина составляет 17",
# 3 это количество элементов, которые были не уникальны,
# Если же длина равна 20 то выведите сообщение "Ваш обьединенный сет полностью уникальный!"
# Необходимо использовать set comprehension, на этапе создания сетов.
# Так же используйте генератор последовательности в comprehension чтобы создать множества из 10 элементов.
# Необходимо использовать set comprehension, на этапе создания сетов.
# Например после использования set comprehension в set1 храниться множество: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# B set2: {8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
# Результат работы программы будет следующий:
# "В этом сете было 2 повторения, его длинна составляет 18"

# import random
# set1 = list(range(1,11))
# set2 = list(range(1,11))
# full_set = set1.union(set2)
# print(full_set)
# a = {set1.pop() for _ in range(10)}
# b = {set2.pop() for _ in range(10)}
# ab = a | b
# n = len(ab)
# print(ab)
# print(f'В этом сете было {20-n} повторения, его длина составляет {n}')
