
# Task 1.

# name_of_friends = ['Erke', 'Ainura', 'Aelita', 'Kamila', 'Aigul']

# for i in name_of_friends:
#     print(i)

# # Task 2.

# labels = ['BMW', 'Lexus', 'Mersedes']
# for i in labels:
#     print(f'I like brand {i}')

# Task 3.

# name_of_list = list('Helloworld!') 
# word1 = name_of_list[:((len(name_of_list)+1)//2)]
# word2 = name_of_list[((len(name_of_list)+1)//2):]

# new_list = word2 + word1
# print(new_list)

# 3.1

# st = list('Helloworld!')
# n = (len(st) // 2) + (len(st) % 2) # к результату деления без остатка + остаток от деления и получается по условию.
# new_list = st[n:] + st[:n] 

# print(new_list)

# 3.2

# name_of_list = ['Hello world!']

# half_length = int((len(name_of_list[0])) / 2)
# chast1 = name_of_list[0][:half_length]
# chast2 = name_of_list[0][half_length:]

# if int(len(name_of_list[0])) % 2 != 0:

#     half_length = int(len(chast1)) + 1


# new_chast1 = name_of_list[0][0:half_length]
# new_chast2 = name_of_list[0][half_length:]
# new_list = new_chast2 + new_chast1
# print(list(new_list))

# Task 4.

# list_ = ['world', 'hello']
# new_list = (list_[1] + ' ' + list_[0]).split(" ")
# print(new_list)

# Task 5.

# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert(0, 'панама')
# print(suitcase)

# Task 6.

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = list()
# for i in nums:
#     if i < 5:
#         res.append(i)
    
# print(res)


# Task 7.

# nums = input()
# nums1 = nums.split(',')
# list_ = list(nums1)
# tuple_ = tuple(nums1)
# print(list_)
# print(tuple_)

# Task 8.

# list_ = [1, 2, 3, 4, 5]
# new_list = list()
# for i in list_:
#     i = str(i)
#     new_list.append(i)

# print(new_list)

# Task 9.

# list_ = [1, 2, 3, 4, 5]
# new_list = list()
# for i in list_:
#     if i % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')

# print(new_list)

# Task 10.

# list_ = list(range(20))
# print(list_)

# Task 11.

# list_ = list(range(0, 101, 2))
# print(list_)

# Task 12

# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 
# list3 = list1 + list2
# print(sum(list3))

# Task 13

# nums = input()
# nums1 = nums.split(',')
# list_ = list(nums1)

# print(sorted(list_))

# Task 14

# variant 1
# list_ = [1, 1, 3]
# if list_[0] == list_[1]:
#     print('yes')
# elif list_[0] == list_[2]:
#     print('yes')
# elif list_[1] == list_[2]:
#     print('yes')
# else:
#     print('ERROR')


# variant 2
# list_ = [1, 1, 3]
# if list_[0] == list_[1] or list_[0] == list_[2] or list_[1] == list_[2]:
#     print('yes')
# else:
#     print('ERROR')

# Task 15

# list_ = []

# for i in range(54,9185):

#    if i % 5 == 0:

#        list_.append(i)

# print(list_)

# nums = list(input('Введите цифры через запятую: '))
# print(nums[0], nums[-1])


"""
1) Напишите программу, которая запрашивает с ввода семь чисел через запятую, добавляет их в список. На экран выводит первое и последнее число списка. Затем удаляет последнее число и вместо него вставляет слово “Makers”.
Например: 
Ввод: Введите цифры через запятую: 5, 7, 8, 1, 3, 0, 8
Вывод: 5 8
[5, 7, 8, 1, 3, 0, ‘Makers’]
"""
nums = input('Введите цифры через запятую: ').split(',')
print(nums[0], nums[-1])
nums.pop()
nums.append('Makers')
print(nums)
"""
2) Напишите программу, которая генерирует 10 случайных чисел, добавляет их в список и возвращает вам список этих чисел в отсортированном виде в порядке возрастания.
"""
# писать код здесь
"""
3) Напишите программу, которая заполняет список словами, введенными с клавиатуры, измеряет длину каждого слова и добавляет полученное значение в другой список. Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'], список длин – [3, 2, 5, 2, 4]. Оба списка должны выводиться на экран.
"""
# писать код здесь