# Task 1

# a = {'x': 1, 'y': 2, 'z': 1}
# a1 = list(a.keys())
# print(a1[1])

# Task 2

# a = {'a': 1, 'b': 2, 'c': 1}
# deleted = a.pop('c')
# print(deleted)

# Task 3

# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)

# Task 4

# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

# Task 5

# a = {'a': 1, 'b': 2, 'c': 1}
# print(list(a.keys()))

# Task 6

# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# Task 7

# a = {'a': 1, 'b': 2, 'c': 1}
# for key in a:
#     print(key)

# Task 8

# a = {'a': 1, 'b': 2, 'c': 1}
# for value in a.values():
#     print(value)

# Task 9

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = a.copy()
# print({key: 2 if val%2 == 0 else val for key, val in b.items()})

# Task 10

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# print({k: v for k, v in a.items() if v})

# Task 11

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# print({key: value / 5 for key, value in a.items()})

# Task 12

# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# print({key: v for key, v in a.items() if v % 2 != 0})

# Task 13

# a = {'a': 1, 'b': 2, 'c': 3} 
# print({val:key for key, val in a.items()})

# Task 14

# a = {'a': 3, 'b': 2}
# print(sum(a.values()))

# Task 15

# a1 = dict({'a': 4, 'b': 5, 'c': 7})
# a2 = {'a': 4, 'b': 5, 'c': 7}
# a3 = dict.fromkeys('abc', 55)
# print(type(a1))
# print(type(a2))
# print(type(a3))

# Task 16

# a = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for val in a:
#     result = result * a[val]
# print(result)




# CLASSWORK 1

# Создайте словарь university, и заполните данными, которые бы отражали количество учащихся 
# на разных факультетах (программирование, экономика, медицина). Внесите изменения в словарь 
# согласно следующему: а) в одном из факультетов изменилось количество учащихся, 
# б) в университете появился новый факультет(лингвистика), 
# с) в университете был расформирован (удален) другой факультет (медицины). 
# Вычислите общее количество учащихся в университете.

# university = {
#     'программирование': 45, 
#     'экономика': 55, 
#     'медицина': 70
# }

# a
# university['программирование'] = 177
# print(university)

# b
# university['лингвистика'] = 89 # 1 sposob
# university.update({'лингвистика': 89}) # 2 sposob
# university.setdefault('лингвистика', 89) # 3 sposob
# print(university)

# c

# university.pop('медицина')
# print(university)
# print(f'Общее количество учащихся составляет: {sum(university.values())}')

# CLASSWORK 2

# Создайте словарь, где ключами являются числа, а значениями – строки. Поменяйте ключи и значения местами.
# Например: исходный словарь - {1: ‘a’, 2: ‘b’, 3: ‘c’}
# На выходе - {‘a’: 1, ‘b’: 2, ‘c’: 3}

# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# print({val: key for key, val in dict_.items()})

# CLASSWORK 3

# Создайте программу, которая запрашивает у вас количество гостей, которых вы хотите пригласить. 
# Далее запрашивает у вас имена гостей поочередно. Как только вы введете последнего гостя 
# программа должна выдать вам список гостей и их порядковые номера в виде словаря.

# guests = int(input('Какое количество гостей вы хотите пригласить? '))
# guests1 = {}
# for i in range(1, guests + 1):
#     name = input('Введите имя гостя: ')
#     guests1.setdefault(i, name)

# print(guests1)

# CLASSWORK 4

# 4) Вы идете в магазин за продуктами. У вас есть список продуктов, 
# в котором перечислены наименования продуктов и количество. Каждый раз, когда вы кладете 
# тот или иной продукт в корзину, вы убираете этот продукт из списка. После того, как ваш 
# список опустеет, вы идете к кассе и расплачиваетесь. Реализуйте данную задачу в вашем коде.

# list_ = [
#     {'картофель': 3},
#     {'огурцы': 4},
#     {'помидоры': 4},
#     {'молоко': 2},
#     {'мясо': 5}
# ]

# while list_:
#     productsssss = input()
#     for product in list_:
#         if productsssss in product:
#             del product[productsssss]
#             print(list_)

#     if not any(list_): 
#         break

# print('Пора идти к кассе')
