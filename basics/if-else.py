# "=============Логические операторы==============="
# # логические операторы - выражения, которые возвращают True, если правда, False - если ложь

# 5 == 5 # True
# 4 == 5 # False

# 5 != 5 # False
# 5 != 2 # True

# 5 > 10 # False
# 10 > 5 # True
# 5 > 5 # False
 
# 5 < 10 # True
# 10 < 5 # False
# 5 < 5 # False

# 5 <= 10 # True
# 10 <= 5 # False
# 5 <= 5 # True

# 5 >= 10 # False
# 10 >= 5 # True
# 5 >= 5 # True

# # "5" = 5 False



# "=========and or==========================="

# "=============And or not================="
# # and - и
# # or - или
# a = 5
# b = 6

# a == 5 and b == 6 # True (правая сторона True, левая тоже True)
# a == 5 and b == 5 # False (правая сторона True, но левая False)
# a == 4 and b == 5 # False (обе стороны False)

# a == 5 or b == 6 # True (правая сторона True, левая тоже True)
# a == 5 or b == 5 # True (правая сторона True, но левая False)
# a == 4 or b == 5 # False (обе стороны False)

# # если обе части выдают True - будет True
# # если обе части выдают False - будет False
# # если одна часть True, вторая False:
# # 1. если стоит and - выйдет False
# # 2. если стоит or - выйдет True

# not True # False
# not False # True
# not a == 5 # False (потому что a == 5)
# not a == 4 # True (потому что a == 5)



# '===================boolean type==============='

# # bool type -  имеет всего 2 значения True & False

# # bool(1) - True
# # bool(0) - False
# # bool(-1)  - True
# #  все числа кроме 0 будут True
# # bool('') - False
# # bool(' ') - True


# # bool(True) - True
# # bool(False) - False

# "===========NoneType================="

# # None - тип данных с одним значением, который используется для обозначения пустых значений или отсутствия значения

# # bool(None)  -   False
# # bool('None')   -   True

# a = None
# # print(bool(a)) False
# # print(a is None) True
# # is - это проверка на полное соответствие


# "===========Условные операторы============"
# # условные операторы нужны для того, чтобы при разных входных данных код работал по разному

# # if условие1:
# #     тело1
# #     # будет работать только если условие1 верно

# # if условие1:
# #     тело1
# #     # будет работать только если условие1 верно
# # else:
# #     тело2
# #     # будет работать если условие1 не верно

# # if условие1:
# #     тело1
# #     # будет работать только если условие1 верно
# # elif условие2:
# #     тело2
# #     # будет работать если условие1 не верно и условие2 верно

# # if условие1:
# #     тело1
# #     # будет работать только если условие1 верно
# # elif условие2:
# #     тело2
# #     # будет работать если условие1 не верно и условие2 верно
# # else:
# #     тело3
# #     # будет работать если условие1 не верно и условие2 не верно


# # в одной конструкции мы можем использовать только один if
# # в одной конструкции мы можем использовать неограниченное кол-во elif или не указывать вообще
# # else мы так-же можем использовать только один раз или не указывать вообще

# a = int(input('Enter: '))

# if a > 0:
#     print(f'Число {a} - положительное')
# elif a < 0:
#     print(f'Число {a} - отрицательное')
# else:
#     print(f'Число {a} - это 0')


# "======FizzBuzz======"
# # выведите числа от 1 до 100
# # если число кратно 3 - вывести Fizz
# # если число кратно 5 - вывести Buzz
# # если число кратно и 5 и 3 - вывести FizzBuzz
# # если число не кратно ни 5 ни 3 - вывести число

# # 1 variant 
# for i in range(1, 101):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print('FizzBuzz')
#         else:
#             print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# # 2 variant
# for i in range(1, 101):
#     if i % 5 == 0:
#         if i % 3 == 0:
#             print('FizzBuzz')
#         else:
#             print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)

# # 3 variant
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)




# # False - 0, "", {}, [], set(), frozenset(), None, False



# x = int(input())
# y = int(input())
# a = x / y
# if x % y == 0:
#     print('x делится на y')
#     print(f'Частное: {a}')
# else:
#     print('')


#     year = int(input())

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')



# num = int(input())

# if num == chr(num):
#     print(f'Это буква {chr(num)}')
# else:
#     print(f'Это не буква, это символ {chr(num)}')

 


 
# num = int(input())

# if (num >= 65 and num <= 90) or (num >= 97 and num <= 122):
#     print(f'Это буква "{chr(num)}"')
# else:
#     print(f'Это не буква, а символ "{chr(num)}"')





#     print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")



# "=========Тернарные операторы========================"
# # условие в одну строчку

# тело1 if условие else тело2

# res = 'Hello' if a == 5 else 'Bye'
# print(res) 
# # 'Hello' если a == 5
# # 'Bye' если a != 5




