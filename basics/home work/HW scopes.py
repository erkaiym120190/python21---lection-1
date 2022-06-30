
# Task 1

# Вам дана вложенная функция:

# def foo():
#     var = 'переменная foo'
  
#     def bar():
#         var = 'переменная bar'
#         . . .
 
#     bar()
# foo()
# print('переменная в foo: ', var)

# Внесите изменения в функции bar таким образом чтобы при вызове функции foo и при попытке распечатать 
# переменную var в глобальной области видимости, выводился следующий результат:
# переменная в foo:  переменная foo
# переменная в foo:  переменная bar

# def foo():
#     global var
#     var = 'переменная foo'

#     def bar():
#         global var
#         print(f'переменная в foo:  {var}')
#         var = 'переменная bar'

#     bar()
# foo()
# print("переменная в foo: ", var)


# Task 2

# У вас есть глоабльная переменная x со значением Я глобальная переменная!. 
# Напишите функцию my_func()которая изменяет значение этой переменной на Я могу изменяться, 
# т.е если вы после вызова функции распечатаете переменную x вне функции она должна возвращать 
# вам значение Я могу изменяться.

# x = 'Я глобальная переменная!'
# print(x)
# def my_func():
#     global x
#     x = 'Я могу изменяться'
#     return

# my_func()
# print(x)
# print(globals())


# Task 3

# Дана глобальная переменная num со значением 3. Напишите функцию mul которая будет возвращать 
# квадрат этой переменной и записывать результат в глобальную переменную num. Вызовите функцию три раза, 
# и распечатайте переменную num.

# mul()
# mul()
# mul()
# print(num)
# Output:

# 6561

# тaк кaк num перезаписали на 9(3*3 = 9) затем на 81

# (99 = 81) и после на 6561(8181 = 6561)


# num = 3

# def mul():
#     global num
#     num = num**2
# mul()
# mul()
# mul()
# print(num)


# Task 4

# Напишите небольшую программу для подсчета доходов и расходов.
# У вас есть глобальная переменная balance = 0 общий счет.
# Программа должна состоять из трех функций: get_salary(amount) - функция для увеличения баланса, 
# которая принимает в аргументы amount - заработная плата и увеличивает переменную balance на число переданное в amount.
# pay_bills(amount, log_name) - уменьшает баланс на количество amount , log_name - принимает строку - 
# на что были потрачены деньги и распечатывает результат, например если мы вызвали pay_bills(300, 'интернет')
# функция распечатывает строку в виде
# "Вы заплатили 300 сом за интернет"
# И функция get_balance(), которая будет распечатывать вам строку:
# У вас на счету `n` сом
# где n - это текущее значение глобальной переменной balance.
# Вызовите функции в данном порядке:

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()
# Результат в консоли:

# У вас на счету 1000 сом
# Вы заплатили 400 сом за кабельное тв
# У вас на счету 600 сом

# Решение

# balance = 0

# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     print(f'У вас на счету {balance} сом')

# get_salary(1000000)
# get_balance()
# pay_bills(450000, 'аренду дома')
# get_balance()


# Task 5

# У вас есть глобальная переменная result = 0. Напишите функции pow_first(x,y), 
# отвечает за первую часть встроенной функции pow и pow_second(z), отвечает за вторую часть pow(z). 
# Вызовите эти функции, а затем выведите переменную result.

# Пример:

# pow_first(2, 3)
# pow_second(3)
# print(result)
# Output:
# 2

# result = 0

# def pow_first(x, y):
#     global result
#     result = x ** y

# def pow_second(z):
#     global result
#     result = result % z
    
# pow_first(2, 3)
# pow_second(3)
# print(result)


# Task 6

# Мурат с друзьями на выходных решил собратся и пойти в ночной клуб.Но в ночной клуб пропускают только тех, кому 17+. 
# Создайте словарь ключами которого являются имена Мурата и его друзей, а значениями являются их возраст.

#  a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# Напишите программу которая определяет кого пустить в ночной клуб а кого нет.

# Output:

# Мурат, Вы можете войти в клуб
# Эржан, Вы можете войти в клуб
# Чынгыз, Вы можете войти в клуб
# Алтынай, Вы можете войти в клуб
# Асема, извините, Вы не проходите по age-control

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}

# def age_control():
#     global a

#     for name, age in a.items():
#         if age < 17:
#             print(f"{name}, извините, Вы не проходите по age-control")
#         else:
#             print(f"{name}, Вы можете войти в клуб")

# age_control()


# Task 7

# Вам дан список a из нескольких имён в нижнем регистре. Напишите программу которая превращает имена из списка в имена, 
# где первая буква имени в верхнем регистре.Запишите результат в новый список b и выведите переменную b.

# Пример:

#  a: ['pipi', 'papa', 'mama']
 
#  b: ['Pipi', 'Papa', 'Mama']

# a = ['pipi', 'papa', 'mama']
# b = list()

# def new_names():
#     global a
#     global b
#     for string in a:
#         string = string.title()
#         b.append(string)
#     print(b)

# new_names()


# Task 8

# Напишите функцию count_symbols() которая принимает строку и возвращает количество гласных, 
# согласных букв и остальных символов. Используйте только кириллические символы. Распечатайте вызов функции.

# Пример:

# print(count_symbols('Мурат супер!'))
# output:

# Количество гласных: 4, согласных: 6, остальных символов: 2


# def count_symbols(string):
#     vowels = 0
#     consonants = 0
#     symbols = 0

#     for a in string:
#         if a in 'уеыоэяиёюа':
#             vowels += 1
#         elif a in 'бвгджйзклмнпрстфхцчшщ':
#             consonants += 1
#         else:
#             symbols += 1
#     return(f'Количество гласных: {vowels}, согласных: {consonants}, остальных символов: {symbols}')


# print(count_symbols('Мурат супер!'))


# 2 способ (пости одно и то же, но есть баг)
# def count_symbols(str_):
#     vowels = 0
#     consonants = 0
#     symbols = 0
    
#     for l in str_.lower():
#         if l in "йуеыаоэяиюё":
#             vowels += 1 
#         elif l in "цкнгшщзмчвфжрлдтсп":
#             consonants += 1
#         else:
#             symbols += 1
#     return f'Количество гласных: {vowels}, согласных: {consonants}, остальных символов: {symbols}'

# print(count_symbols('Мурат супер'))


# Task 9

# Создайте пустой список a. Напишите программу которая должна записывать в ваш список числа от 0 до 10. 
# Распечатайте переменную a.

# a = list()
# for i in range(0, 11):
    # a.append(i)
# print(a)


# Task 10

# Определите перемнную a в котором будут хранится список из целых чисел.
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# Напишите программу которая выводит все элементы этого списка, которые меньше 7.


# 1 способ
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# b = []
# for i in a:
#     if i < 7:
#         b.append(i)
# print(b)

# 2 способ
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]

# for elem in a:
#     if elem < 7:
#         print(elem)



# CLASS WORK TASK 1

# Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. 
# Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, 
# который определен в этой функции. То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.

# size_first_matryoshka = 10
# def two_matryoshka():
#    size_matryoshka_two = 5
#    def three_matryoshka():
#        size_matryoshka_three = 3
#        return size_matryoshka_three + size_matryoshka_two
#    return three_matryoshka() + size_first_matryoshka
# print(two_matryoshka())



# CLASS WORK  TASK 2

# Есть глобальная переменная, которая содержит пустой список. Вам необходимо написать функции, 
# одна из которых add() - добавляет в этот список имена, которые вводит пользователь. 
# А другая функция remove() - удаляет эти имена из списка по индексу, который вводит пользователь. 
# Вызовите функции в рандомном порядке 10 раз и в конце выведите список.


# global_ = list()
# def add(name):
#     global global_
#     global_ += [name]

# def remove(inx):
#     del global_[inx]

# for i in range(7):
#     add(input())

# for i in range(2):
#     remove(int(input()))

# print(global_)


# gl = []

# def add(name):

#    global gl

#    gl += [name]

# def remove(inx):

#    del gl[inx]

# for _ in range(7):

#    add(input())

# for _ in range(2):

#    remove(int(input()))

# print(gl)



# from random import choice
 
# def add():
#     global c
#     c.append(input('Введите имя '))
#     return 1
 
# def remove():
#     global c
#     if not len(c): return
#     del c[int(input(f'Удалить имя от 0 до {len(c) - 1} '))]
#     return 1
 
# c = []
# i = 0
# while i < 10:
#     if choice([add, remove])():
#         i += 1
# print(c)



"Айгерим разбор в мини -группах 24.06.2022"


# list_ = [1, 2, 3, 4, 5, 6, 7]

# list2 = [i**2 if i >3 else i for i in list_ if i % 2 != 0]
# print(list2)   #    [1, 3, 25, 49]



# dict_ = {'a': 3, 'b': 4, 'c': 5}

# dict2 = {k : v + 1 if v > 3 else v for k, v in dict_.items()}
# print(dict2)  #      {'a': 3, 'b': 5, 'c': 6}  



"Вложенные словари"

# dict_ = {'a': {'z': 1}, 'b': {'y': 2}, 'c': {'r': 3}}

# dict2 = {k : inner_v 
# for k, v in dict_.items() 
# for inner_v in v.values()}

# print(dict2)


# r = 'global'
# def func():
#     r = 'enclosed'
#     print(r)
#     def func1():
#         print(r)
#         # r = 'local'

#     func1()
# print(r)
# func()



# try:
#    word = int(input())
# except:
#     print('error')
# else:
#     print('else')
# finally:
#     print('closed')


