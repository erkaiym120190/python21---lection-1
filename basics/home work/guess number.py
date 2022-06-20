# import random
# guesses_made = 0
# name = input('Здравствуйте! Как вас зовут? ')
# number = random.randint(1, 30)
# print(f'Отлично, {name}, я загадал число, которое находится между 1 и 30. Увас будет 5 попыток. Сможете угадать?')

# while guesses_made < 5:
#     guess = int(input('Введите число: '))
#     guesses_made += 1
#     if guess < number:
#         print('Ваше число меньше того, что я загадал.')
#     elif guess > number:
#         print('Ваше число больше того, чем я загадал.')
#     elif guess == number:
#         break
#     elif guess == number:
#         print(f'Вау, {name}! Вы угадали мое число, использовав {guesses_made} попыток!')  
#     # elif guess == number:
#     #     break
#     elif guess != number:
#         number = str(number)
#         print(f'А вот и не угадали! Я загадал число {number}.')

# 2 sposob

# import random

# compGuess = random.randint(1, 30)
# userGuess = 0
# name = input('Приветствую! Давайте сыграем в игру. Как вас зовут? ')

# while userGuess != compGuess:
#     userGuess = int(input(f'{name}, введите ваше число от 1 до 30: '))
#     if userGuess < compGuess:
#         print('Число должно быть больше!')
#     elif userGuess > compGuess:
#         print('Число должно быть меньше!')
#     else:
#         print('Вы угадали, это число ' + str(userGuess))


# Самостоятельные таски

# 1

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for elem in a:
#     if elem < 5:
#         print(elem)

# 2

# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# result = [elem for elem in a if elem in b]
# print(result)

# 3

# a = [1,1,2,3,5,8,13,21,34,55,89]
# print(sorted(a))
# print(sorted(a,reverse=True))

# 4 list

# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# c = [1,'dfd', 34,54,67,'hjh', 65]
# result = a + b + c
# print(result)

# 4 dict

# a = {1:'a',2:'d'}
# dict_ = {"a":"hello", "b":6, "c":3}
# dict1_ = {"v":2, "n":3, "k":4}
# dict_.update(a)
# dict_.update(dict1_)
# print(dict_)

# 5

# a = [1,1,2,3,5,8,13,21,34,55,89]
# a.append('str')
# print(a)
# a[5] = 123
# print(a)
# a.append([9,8,7])
# print(a)
# a.append((23,45,67))
# print(a)
# print(a[-2])
# del a[-1]
# print(a)
# a.count(1)
# print(a.count(1))

# 6

# a = [1,1,2,3,5,8,13,21,34,55,89]
# print(a[0], a[-1])

# 7

# a = 'str'
# b = 123

# a, b = b, a
# print(a, b)

# 8

# lst = [0,0,1,2,3,4,5,5,6,7]
# st = set(lst)
# print(len(st) == len(lst))

# 9

# my_dict_ = {'a':500, 'b':5874, 'c':560, 'd': 400, 'e':5874, 'f':20}
# my_dict_.update({'str':123})
# print(my_dict_)
# my_dict_.update({(1,2,3):[23,45,67]})
# print(my_dict_)
# print(my_dict_.get('e'))
# print(my_dict_.keys())

# 10

# st = {'it','is','set',1}
# frozen_st = frozenset({'it','is','frozen','set',2})
# # Выполняем операцию объединения множеств.
# # Результатом объединения будет множество, содержащее все элементы обоих множеств(без дубликатов)
# union = st | frozen_st
# print(union)
# # Выполняем операцию пересечение множеств. 
# # Результатом пересечения будет множество, содержащее элементы, присутствующие в обоих множествах
# intersection = st & frozen_st
# print(intersection)

# 11

# list_ = [1,2,3,4,5,6,5,4,3,45,43,58,98,83,56,78,32,44,23,55,67,54,56,54]
# list_[20] = 200
# print(list_)


import random

compGuess = random.randint(1,30)
userGuess = 0
name = (input('Привет!!! Давайте сыграем в игру "Угадай число". Как вас зовут? '))

while userGuess != compGuess:
    userGuess = int(input(f'{name}, введите ваше число от 1 до 30: '))
    if userGuess > compGuess:
        print(f'{name}, число должно быть меньше!')
    elif userGuess < compGuess:
        print(f'{name}, число должно быть больше!')
    else:
        print(f'{name}, вы угадали! Это число ' + str(compGuess))