# comprehension - специальная конструкция, с помощью которой 
# можно по определенным правилам создавать списки и словари
# генерация последовательностей в одну строку, используя цикл

# 1 вариант - действие for элемент in итерируемый объект
# 2 вариант - действие for элемент in итерируемый объект if фильтр 

# for

# list_ = list()
# for num in range(1, 21):
#    list_.append(num * 2)
# print(list_)

# list comprehension

# list_ = [num * 2 for num in range(1, 21)]
# print(list_)

# list_users = ['Alice', 'Sam', 'Sandy', 'Ben', 'john']
# invitations = ['You are invited ' + name for name in list_users]
# print(invitations)


# list1 = [10, 5, -6, -8, 12, 20, 3, 14, 4] 
# list2 = [num for num in list1 if num % 2 == 0]
# print(list2)

# ]

# list1 = [10, 5, -6, -8, 12, 20, 3, 14, 4]
# list2 = [num for num in list1 if num % 2 == 0 and num > 0]
# print(list2)

# list1 = [10, 5, -6, -8, 12, 20, 3, 14, 4]
# list2 = [num for num in list1 if num % 2 == 0 or num % 3 == 0]
# print(list2)

# strings = ['1998', '2001y', '2008year', '2020']
# list_ = [year for year in strings if year.isdigit()]
# print(list_)

# list_ = ['Raychel', 'John', 'Alice', 'Sam']
# list_ = [len(name) for name in list_]
# print(list_)

# list_ = [-5, -12, 0, 1, -2, 8, 4, 5, 7]
# list_ = [num if num < 0 else num ** 2 for num in list_]
# print(list_)

# "============Comprehension================"
# comprehension - генерация последовательностей в одну строку используя цикл

# 1. результат for элемент in итерируемый объект
# 2. результат for элемент in итерируемый объект if фильтр

# "==============List comprehension================"

# "создать список состоящий из чисел от 1 до 10 умноженных на 2"
# list_ = []
# for i in range(1, 11):
#     list_.append(i*2)
# # list_ = [1,4,6,8,10,12,14,16,18,20]

# list_ = list( (i*2 for i in range(1,11)) )
# # list_ = [1,4,6,8,10,12,14,16,18,20]

# list_ = [i*2 for i in range(1,11)]
# # list_ = [1,4,6,8,10,12,14,16,18,20]

# "создать список состоящий из четных чисел от 1 до 10"
# list_ = []
# for i in range(1,11):
#     # if not 0 (четное)
#     if not i % 2: 
#         list_.append(i)

# list_ = [i for i in range(1,11) if not i%2]

# list_ = [i for i in range(2,11,2)]

# # list_ = [2,4,6,8,10]

# [print(i) for i in range(10)]
# # [None, None, None, None, None, None, None, None, None, None]

# list_ = ["hello" for i in range(10)]
# # ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"]

# print([input() for i in range(10)])
# # на каждой итерации запрашивает инпут


# "создать список состоящий из чисел от 1 до 10, но вместо чисел написать 'четное' или 'нечетное'"

# list_ = [ 'нечетное' if i % 2 else 'четное' for i in range(1,11) ]
# # ['нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное']


# "создать список из чисел, находящихся в list1, заменив их на 'четное' или 'нечетное'"
# list1 = [1,'hello', 3, 'a', 4.0, 6, 8, 'hw']
# [ 'нечетное' if i % 2 else 'четное'
#   for i in list1 
#   if type(i) == int or type(i) == float ]


# "=============Dict comprehension=================="
# 'создать словарь, где ключи - числа от 1 до 10, а значения эти числа ввиде строки'
# dict_ = dict( (i, str(i)) for i in range(1,11) )
# # {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

# 'даны 2 списка, создайте словарь, где ключи - элементы 1 списка, а значения - второго'
# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']

# dict_ = dict( (list1[index], list2[index]) for index in range(len(list1)) )
# # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# dict_ = { list1[index]: list2[index] for index in range(len(list1)) }
# # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# 'создайте копию словаря'
# dict1 = {"a":1, "b":2, 4:"c"}
# dict2 = { key: value for key, value in dict1.items() }
# # {"a":1, "b":2, 4:"c"}

# 'поменяйте ключ и значение местами'
# dict1 = {"a":1, "b":2, 4:"c"}
# dict2 = { value : key for key, value in dict1.items() }
# # {1:"a", 2:"b", "c":4}

# 'дан словарь, где значения - список с числами, создайте новый словарь, где значения - сумма тех чисел'
# dict1 = {
#     "a":[1,2,3,4,5],
#     "b":[10,30,2,5],
#     "c":[74,28,47],
#     "d":[4,6,2,92,9]
#     }
# dict2 = { key: sum(value) for key, value in dict1.items() }
# # {'a': 15, 'b': 47, 'c': 149, 'd': 113}


# "================Вложенные comprehensions===================="
# 'создайте словарь, где ключами будут числа от 1 до 5, а значениями списки от 1 до числа (который ключ)'

# dict_ = { i: list(range(1, i+1)) for i in range(1,6) }
# # {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}
# dict_ = { i: [j for j in range(1, i+1)] for i in range(1,6) }
# # {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

# 'создайте список, состоящий из 10 списков, в которых строка "hello world" повторяется 5 раз'

# list_ = [
#     [i for i in range(5)]
#     for i in range(10)
# ]
# # [[0, 1, 2, 3, 4], 
# # [0, 1, 2, 3, 4], 
# # [0, 1, 2, 3, 4], 
# # [0, 1, 2, 3, 4], 
# # [0, 1, 2, 3, 4], 
# # [0, 1, 2, 3, 4], 
# # [0, 1, 2, 3, 4], 
# # [0, 1, 2, 3, 4], 
# # [0, 1, 2, 3, 4], 
# # [0, 1, 2, 3, 4]]





# 3 
# dict.get(key)
# dict(key)
# dict.keys() # все ключи
# dict.values() # все значения
# dict.items() # вообще все

# dict.pop(key)




